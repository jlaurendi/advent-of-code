use std::fs;

fn parse_input(contents: &str) -> Vec<Vec<i32>> {
    contents
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<i32>().expect("Failed to parse number"))
                .collect()
    })
    .collect()
}

fn part1(input: &Vec<Vec<i32>>) -> i32 {
    let mut num_safe = 0;
    for row in input {
        let mut safe = true;
        let mut prev = nil;
        let mut curr = nil;
        for num in row {
            print!("{} ", num);
        }

        if safe {
            num_safe += 1;
        }
    }
    return num_safe;
}

fn part2(input: &Vec<Vec<i32>>) -> i32 {
    return 0;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = fs::read_to_string("src/bin/input/02.txt").expect("Failed to read file");
    let input = parse_input(&contents);
    
    let part1_result = part1(&input);
    println!("Part 1: {}", part1_result);

    let part2_result = part2(&input);
    println!("Part 2: {}", part2_result);

    Ok(())
}