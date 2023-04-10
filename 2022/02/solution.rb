class AOCClass
    @@shape_scores = {
        'X' => 1,
        'Y' => 2,
        'Z' => 3
    }
    @@outcome_scores = {
        'A' => {
            'X' => 3,
            'Y' => 6,
            'Z' => 0
        },
        'B' => {
            'X' => 0,
            'Y' => 3,
            'Z' => 6
        },
        'C' => {
            'X' => 6,
            'Y' => 0,
            'Z' => 3
        }
    }

    def compute_score(input)
        score = 0
        input.each_line do |line|
            one, two = line.split()
            score += @@outcome_scores[one][two] + @@shape_scores[two]
        end
        score
    end

    def part_one(input)
        score = compute_score(input)
        return score
    end

    @@part2_map = {
        'A' => {
            'X' => 'Z',
            'Y' => 'X',
            'Z' => 'Y'
        },
        'B' => {
            'X' => 'X',
            'Y' => 'Y',
            'Z' => 'Z'
        },
        'C' => {
            'X' => 'Y',
            'Y' => 'Z',
            'Z' => 'X'
        }
    }

    @@part2_map2 = {
        'X' => 0,
        'Y' => 3,
        'Z' => 6
    }
    def compute_score2(input)
        score = 0
        input.each_line do |line|
            one, two = line.split()
            move = @@part2_map[one][two]
            score += @@part2_map2[two] + @@shape_scores[move]
        end
        score
    end

    def part_two(input)
        score = compute_score2(input)
        return score
    end

end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"

# part 2
# 11614 too low

# part 1
# 8634 too low
# 9679 too low