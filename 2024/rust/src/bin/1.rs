use std::fs;
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file_path = Path::new("src/bin/input/01.txt");
    let contents = fs::read_to_string(file_path).expect("Failed to read file");
    // println!("{}", contents);

    let number_pairs: Vec<(i32, i32)> = contents
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            let nums: Vec<i32> = line
                .split_whitespace()
                .map(|num| num.parse::<i32>().expect("Failed to parse number"))
                .collect();

            (nums[0], nums[1])
        })
        .collect();

    let (mut left, mut right): (Vec<i32>, Vec<i32>) = number_pairs.into_iter().unzip();
    left.sort();
    right.sort();
    
    let mut result = 0;
    for (a, b) in left.iter().zip(right.iter()) {
        result += (a - b).abs();
    }
    println!("Part 1: {}", result);
    Ok(())
}