use std::fs;
use std::path::Path;
use std::collections::HashMap;

fn parse_input(contents: &str) -> (Vec<i32>, Vec<i32>) {
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

    return number_pairs.into_iter().unzip()
}

fn part1(left: &[i32], right: &[i32]) -> i32 {    
    let mut result = 0;
    for (a, b) in left.iter().zip(right.iter()) {
        result += (a - b).abs();
    }
    return result;
}

fn part2(left: &[i32], right: &[i32]) -> i32 {
    let mut left_counts: HashMap<i32, i32> = HashMap::new();
    let mut right_counts: HashMap<i32, i32> = HashMap::new();
    for left_num in left.iter() {
        *left_counts.entry(*left_num).or_insert(0) += 1;
    }
    for right_num in right.iter() {
        *right_counts.entry(*right_num).or_insert(0) += 1;
    }

    // println!("{:?}", left_counts);
    // println!("{:?}", right_counts);

    let mut result: i32 = 0;
    for (num, left_count) in left_counts.iter() {
        if right_counts.contains_key(num) {
            let right_count = right_counts.get(num).unwrap();
            result += num * left_count * right_count;
        }
    }
    return result;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file_path = Path::new("src/bin/input/01.txt");
    // let file_path = Path::new("src/bin/input/01-example.txt");

    let contents = fs::read_to_string(file_path).expect("Failed to read file");

    let (mut left, mut right) = parse_input(&contents);
    left.sort();
    right.sort();

    let part1_result = part1(&left, &right);
    println!("Part 1: {}", part1_result);

    let part2_result = part2(&left, &right);
    println!("Part 2: {}", part2_result);

    Ok(())
}