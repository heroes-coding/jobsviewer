
use rusqlite::Connection;
use std::path::Path;
use strsim::{jaro_winkler};

pub fn initialize_db(path: &str) -> Connection {
    let existed_previously = Path::new(path).exists();
    let conn = Connection::open(path).unwrap();
    if !existed_previously {
        conn.execute("CREATE TABLE existing (
                id              INTEGER PRIMARY KEY
                )", &[]).unwrap();
        conn.execute("CREATE TABLE listings (
                id              INTEGER PRIMARY KEY,
                region          TEXT NOT NULL,
                state           TEXT NOT NULL,
                location        TEXT NOT NULL,
                title           TEXT NOT NULL,
                link            TEXT NOT NULL,
                timestamp       INTEGER NOT NULL,
                html            TEXT NOT NULL,
                body            TEXT NOT NULL
                )", &[]).unwrap();
        conn.execute("CREATE TABLE categories (
                category        TEXT NOT NULL,
                region          TEXT NOT NULL,
                state           TEXT NOT NULL,
                url             TEXT NOT NULL,
                count           INTEGER NOT NULL
                )", &[]).unwrap();
        conn.execute("CREATE INDEX i_titles ON listings (title);", &[]).unwrap();
        conn.execute("CREATE INDEX i_timestamp ON listings (timestamp);", &[]).unwrap();
    }
    return conn
}


#[derive(Debug)]
struct ID {
    id: i64
}



pub fn has_existing(conn: &Connection, id: i64) -> bool {
    let mut stmt = conn.prepare("SELECT * FROM existing WHERE id = ?").unwrap();
    let id_iter = stmt.query_map(&[&id], |row| { ID { id: row.get(0) } }).unwrap();
    if id_iter.count() == 1 { return true }
    return false;
}

pub fn print_listings(min_timestamp: i64, db_path: &str) {
    let conn = initialize_db(db_path);
    let mut stmt = conn.prepare("SELECT * FROM listings WHERE timestamp > ?").unwrap();
    let listing_iter = stmt.query_map(&[&min_timestamp], |row| ::Listing {
            job: row.get(4),
            link: row.get(5),
            id: row.get(0),
            timestamp: row.get(6),
            loc: row.get(3),
            region: row.get(1),
            state: row.get(2),
            html: row.get(7),
            text: row.get(8),
        }).unwrap();

    for listing in listing_iter {
        let json_job = format!("{}",::serde_json::to_string(&listing.unwrap()).unwrap());
        println!("{}",json_job);
    }
}

pub fn add_existing(conn: &Connection, id: i64) {
    let mut stmt = conn.prepare("INSERT INTO existing (id) VALUES (:id)").unwrap();
    stmt.execute_named(&[(":id", &id)]).unwrap();
}

pub fn add_listing(conn: &Connection, listing: &::Listing, region: String, state: String ) {
    conn.execute("INSERT INTO listings (id, region, state, location, title, link, timestamp, html, body)
                  VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)",
                 &[&listing.id, &region, &state, &listing.loc, &listing.job, &listing.link, &listing.timestamp, &listing.html, &listing.text]).unwrap();
}

pub fn listing_is_duplicate(conn: &Connection, listing: &::Listing) -> bool {
    let mut stmt = conn.prepare("SELECT id, title, timestamp, body FROM listings WHERE title = ?").unwrap();
    let previous_iter = stmt.query_map(&[&listing.job], |row| {  
        let prev_text : String = row.get(3);
        return prev_text;
    }).unwrap();
    for body in previous_iter {
        if jaro_winkler(&body.unwrap(), &listing.text) > 0.95 { return true; } 
    }
    return false;
}
