class AOCClass
    def parse_grid(input)
        grid = []
        input.each_line do |line|
            next_row = []
            line = line.strip()
            line.each_char do |char|
                next_row.push(char.to_i) 
            end
            grid.push(next_row)
        end
        grid
    end

    def print_grid(grid)
        for i in 0..grid.length-1
            puts grid[i].join("")
        end
    end

    def check_visible(grid, x, y)
        val = grid[x][y]
        length = grid.count
        width = grid[0].count

        if x == 0 || y == 0 || x == length - 1 || y == width - 1
            return true
        end

        # check left
        vis_left = true
        for i in 0..x-1
            if grid[i][y] >= val
                vis_left = false
                break
            end
        end

        # check right
        vis_right = true
        for i in x+1..length-1
            if grid[i][y] >= val
                vis_right = false
                break
            end
        end

        # check top
        vis_top = true
        for j in 0..y-1
            if grid[x][j] >= val
                vis_top = false
                break
            end
        end

        # check bottom
        vis_bottom = true
        for j in y+1..width-1
            if grid[x][j] >= val
                vis_bottom = false
                break
            end
        end

        # puts vis_left, vis_right,vis_top,vis_bottom
        return vis_left || vis_right || vis_top || vis_bottom
    end

    def get_count_in_range(grid, x, y, start, stop, dir1, dir2)
        tree_height = grid[x][y]

        count = 0
        max_elt = -1
        # for i in 0..x-1
        for i in start..stop
            idx = dir2 == 'normal' ? i : stop - i
            curr_height = dir1 == 'horizontal' ? grid[idx][y] : grid[x][idx]
            count += 1
            if curr_height >= max_elt
                max_elt = curr_height
                if max_elt == 9 || max_elt >= tree_height
                    break 
                end
            end
        end
        return count
    end

    def calculate_scenic_score(grid, x, y)
        length = grid.count
        width = grid[0].count

        # if x == 0 || y == 0 || x == length - 1 || y == width - 1
        #     return 0
        # end

        # left
        left = get_count_in_range(grid, x, y, 0, x-1, 'horizontal', 'reverse')
        right = get_count_in_range(grid, x, y, x+1, length-1, 'horizontal', 'normal')
        top = get_count_in_range(grid, x, y, 0, y-1, 'vertical', 'reverse')
        bottom = get_count_in_range(grid, x, y, y+1, width-1, 'vertical', 'normal')

        # puts "#{left}, #{right}, #{top}, #{bottom}"
        return left * right * top * bottom
    end

    def part_one(input)
        grid = parse_grid(input)
        length = grid.count
        width = grid[0].count
        num_visible = 0

        # puts check_visible(grid, 1, 3)
        # exit 1
        for i in 0..length-1
            for j in 0..width-1
                if check_visible(grid, i, j)
                    num_visible += 1
                    # puts "#{i}, #{j}, #{grid[i][j]}"
                end
            end
        end
        return num_visible
    end

    def part_two(input)
        grid = parse_grid(input)
        # puts print_grid(grid)
        # exit 1
        length = grid.count
        width = grid[0].count

        # calculate_scenic_score(grid, 2, 3)
        # exit 1
        scores = []
        for i in 0..length-1
            for j in 0..width-1
                score = calculate_scenic_score(grid, i, j)
                # puts "#{i}, #{j}: #{score}"
                # if score == 1800
                #     puts "Score 1800! (#{i}, #{j})"
                #     puts grid[i][j]
                #     puts grid[i].join("")
                #     col = grid.map{ |row| row[j] }
                #     puts col.join("")
                # end
                scores.append(score)
            end
        end

        # puts scores.inspect
        return scores.max
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
# input = "3037345
# 2551245
# 6533234
# 3354945
# 3539067
# 4567898
# 5123459"
# puts input
# input = "30373
# 25512
# 65332
# 33549
# 35390"
# puts input
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"

# part one
# 2663 too high
# 1362 too low

# part two
# 1800 too low
# 4900 too low
