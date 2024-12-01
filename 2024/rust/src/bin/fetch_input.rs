use reqwest::header::COOKIE;
use std::env;
use std::fs;
use std::path::Path;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Get environment variable
    let session_cookie = env::var("AOC_SESSION_COOKIE").expect("Please set AOC_SESSION_COOKIE as an environment variable.");

    // Get year and day from command-line arguments
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: fetch_input YEAR DAY");
        return Ok(());
    }

    let year: i32 = args[1].parse().expect("Year must be a valid 4-digit integer.");
    let day: i32 = args[2].parse().expect("Day must be a valid integer between 1 and 31.");

    if year < 2000 || year > 9999 {
        panic!("Year must be a 4-digit integer greater than 2000.");
    }
    if day < 1 || day > 31 {
        panic!("Day must be a valid integer between 1 and 31.");
    }

    // Format the day string (e.g., "01" for day 1)
    let day_string = format!("{:02}", day);

    // Fetch the input
    let url = format!("https://adventofcode.com/{}/day/{}/input", year, day);
    let client = reqwest::Client::new();
    let response = client
        .get(&url)
        .header(COOKIE, format!("session={}", session_cookie))
        .send()
        .await?;

    if !response.status().is_success() {
        panic!(
            "Failed to fetch input: {} {}",
            response.status(),
            response.text().await?
        );
    }

    let input = response.text().await?;

    // Create directory and save input
    let directory = Path::new(&day_string);
    let input_file = directory.join("input.txt");

    fs::create_dir_all(&directory)?;
    fs::write(&input_file, input)?;

    // Create a solution file if it doesn't exist
    let solution_file = directory.join("solution.rs");
    if !solution_file.exists() {
        let template = "// Write your solution here\nfn main() {}";
        fs::write(&solution_file, template)?;
    }

    println!("Input saved to {}", input_file.display());
    Ok(())
}
