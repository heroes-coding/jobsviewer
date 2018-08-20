/// Takes in simple command line arguments for either 
///     1) Getting new listings from a craigslist jobs page and printing the new ones, or:
///     2) Printing all old listings within x number of days

extern crate reqwest;
extern crate select;
extern crate chrono;
extern crate rusqlite;
extern crate strsim;
extern crate serde;
extern crate serde_json;

#[macro_use]
extern crate serde_derive;

use select::document::Document;
use select::predicate::{Class, Name};
use chrono::prelude::*;
use std::io::{self, Write};

pub mod database;

static START_BODY_MARKER: &'static str = "Link to This Post";
static END_BODY_MARKER: &'static str = "Principals only. Recruiters,";

#[derive(Debug, Serialize, Deserialize)]
pub struct Listing {
    pub job: String,
    pub link: String,
    pub id: i64,
    pub timestamp: i64,
    pub loc: String,
    pub region: String,
    pub state: String,
    pub html: String,
    pub text: String
}



/// Prints usage instructions with all of the necessary command line arguments for two functions
/// ```
/// print_instructions()
/// ```
fn print_instructions() {
    println!("Run with the following arguments:
        1 For new listings + the following (5 arguments total)
        full job listings link
        region
        state
        database location on disk
        OR 2 For old listings + the following:
        days since posting
        ");
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    // println!("There are {} args",args.len());
    if args.len() < 4 {
        print_instructions();
    } else if args[1] == "1" {
        if args.len() != 6 { print_instructions(); }
        else {
            // println!("Should be calling scrape_listings");
            // println!("Args: {:?}",args);
            let result = scrape_listings(&args[2],&args[3],&args[4],&args[5]);
            // println!("Result was: {}",result);
        }
    } else if args[1] == "2" {
        if args.len() != 4 { print_instructions(); }
        else {
            let min_timestamp = Utc::now().timestamp() - 60*60*24*args[2].parse::<i64>().unwrap();
            // println!("Min timestamp is: {}",min_timestamp);
            database::print_listings(min_timestamp,&args[3]);
        }
    } else { print_instructions(); }

}

fn get_listings(document: Document, region: &str, state: &str) -> Vec<Listing> {
    let mut listings: Vec<Listing> = vec![];
    for row in document.find(Class("result-row")) {
        // grabbing the story rank
        match row.find(Class("result-hood")).next() {
            Some(t) => {
                let loc = format!("{}",t.text().replace("(", "").replace(")", "").trim());
                let job_info =  row.find(Class("hdrlnk")).next().unwrap();
                let job = job_info.text();
                let link = job_info.attr("href").unwrap();
                let time = row.find(Name("time")).next().unwrap().attr("datetime").unwrap();
                let date = Utc.datetime_from_str(time, "%Y-%m-%d %H:%M").unwrap();
                // let date = DateTime::parse_from_str(time, "%Y-%m-%d %H:%M");
                let link_parts = link.split("/").collect::<Vec<_>>();
                let id_parts = link_parts[link_parts.len() - 1].split(".html").collect::<Vec<_>>();
                let id : i64 = id_parts[0].parse().unwrap();
                let mut listing = Listing { job, link: link.to_string(), id, timestamp: date.timestamp(), 
                    loc, region: region.to_string(), state: state.to_string(), html: "".to_string(), text: "".to_string() };
                listings.push(listing);
                // println!("Job: {:?}, link: {:?}, time: {:?}, id: {:?}, loc: {:?}",job,link,date,id,loc);
            },
            None => continue,
        };
        // println!("Listings: {:?}",listings);
    }
    listings
}

fn get_post(mut listing: Listing) -> Option<Listing> {
    let resp = reqwest::get(&listing.link);
    if resp.is_err() { return None };
    let doc = Document::from_read(resp.unwrap());
    if doc.is_err() { return None };
    let doc = doc.unwrap();
    let node = doc.find(Class("userbody")).next().unwrap();
    let mut text = str::replace(&node.text(), "\n", "");
    if text.contains(START_BODY_MARKER) { text = text.split(START_BODY_MARKER).collect::<Vec<_>>()[1].to_string(); }
    if text.contains(END_BODY_MARKER) { text = str::replace(text.split(END_BODY_MARKER).collect::<Vec<_>>()[0],END_BODY_MARKER,""); }
    text = text.trim().to_string();
    let html = node.html();
    listing.html = html;
    listing.text = text;
    return Some(listing)
}

fn scrape_listings(url: &str, region: &str, state: &str, db_path: &str) -> u8 {

    let resp = reqwest::get(url);
    if resp.is_err() {
        println!("{:?}",resp.unwrap_err());
        return 1 
    };

    let doc = Document::from_read(resp.unwrap());
    if doc.is_err() { return 2 };

    let listings = get_listings(doc.unwrap(), region, state);
    let conn = database::initialize_db(db_path);

    for listing in listings {
        let exists = database::has_existing(&conn, listing.id);
        if exists { continue; } 
        else {     
            let listing = get_post(listing).unwrap();
            database::add_existing(&conn,listing.id); 
            let dup = database::listing_is_duplicate(&conn, &listing);
            if dup { 
                continue;
            } else {
                database::add_listing(&conn, &listing, region.to_string(), state.to_string() );
                let json_job = format!("{}",serde_json::to_string(&listing).unwrap());
                println!("{}",json_job);
            }
        }

    }
    return 0
  
}