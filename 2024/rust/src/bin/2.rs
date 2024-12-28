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
        let is_safe_increasing = check_is_safe(&row, true, None);
        let is_safe_decreasing = check_is_safe(&row, false, None);
        let is_safe = is_safe_increasing.is_safe || is_safe_decreasing.is_safe;
        if is_safe {
            num_safe += 1;
        }
    }
    return num_safe;
}

struct IsSafeResult {
    is_safe: bool,
    idx: usize
}

fn check_is_safe(row: &Vec<i32>, dir: bool, idx_to_skip: Option<usize>) -> IsSafeResult {
    let dir_multiplier = if dir { 1 } else { -1 };
    let min_diff = 1;
    let max_diff = 3;
    for i in 0..row.len() - 1 {
        let mut idx1 = i;
        let mut idx2 = i + 1;

        match idx_to_skip {
            Some(idx) => {
                if idx == i {
                    if idx == 0 {
                        continue
                    } else {
                        idx1 -= 1;
                    }
                }
                if idx == i + 1 {
                    idx2 += 1;
                }
            },
            None => {}
        }

        if idx2 >= row.len() {
            continue;
        }

        let diff = (row[idx1] - row[idx2]) * dir_multiplier;


        if diff > max_diff || diff < min_diff {
            return IsSafeResult { is_safe: false, idx: i };
        }
    }
    return IsSafeResult { is_safe: true, idx: 0 };
}

fn part2(input: &Vec<Vec<i32>>) -> i32 {
    let mut num_safe = 0;
    for row in input {
        let is_safe_increasing = check_is_safe(&row, true, None);
        let is_safe_decreasing = check_is_safe(&row, false, None);
        let is_safe = is_safe_increasing.is_safe || is_safe_decreasing.is_safe;
        if is_safe {
            num_safe += 1;
        } else {
            let is_safe_increasing2 = check_is_safe(&row, true, Some(is_safe_increasing.idx));
            let is_safe_decreasing2 = check_is_safe(&row, false, Some(is_safe_decreasing.idx));
            let is_safe2 = is_safe_increasing2.is_safe || is_safe_decreasing2.is_safe;
            if is_safe2 {
                num_safe += 1;
            }

            if !is_safe2 {
                let is_safe_increasing3 = check_is_safe(&row, true, Some(is_safe_increasing.idx+1));
                let is_safe_decreasing3 = check_is_safe(&row, false, Some(is_safe_decreasing.idx+1));
                let is_safe3 = is_safe_increasing3.is_safe || is_safe_decreasing3.is_safe;
                if is_safe3 {
                    num_safe += 1;
                }
            }
        }
    }
    return num_safe;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let contents = fs::read_to_string("src/bin/input/02.txt").expect("Failed to read file");
    // let contents = fs::read_to_string("src/bin/input/02-example.txt").expect("Failed to read file");
    let input = parse_input(&contents);
    
    let part1_result = part1(&input);
    println!("Part 1: {}", part1_result);

    let part2_result = part2(&input);
    println!("Part 2: {}", part2_result);

    Ok(())
}

// 542 - too low