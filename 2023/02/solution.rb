class AOCClass
    def parse(input)
        games = []
        input.each_line do |line|
            game = line.split(":")[1].split(';').map{|x| x.strip }
            game = game.map{|x| x.split(", ")}.map{|x| x.map{ |y| y.split(" ") } }
            game.map do |x|
                x.each do |y|
                    y[0] = y[0].to_i 
                end
            end

            games.append(game)
        end
        return games
    end

    def part_one(input)
        games = parse(input)
        red_max, green_max, blue_max = 12, 13, 14
        count = 0
        # puts "Game len #{games.length}"
        for i in 0...games.length
            success = true
            # puts "Game: #{games[i].inspect}"
            game = games[i]
            for j in 0...game.length
                # puts "this: #{games[i][j]}"
                move = game[j]
                for k in 0...move.length
                    val, color = move[k]
                    # puts val, color
                    if color == 'red' && val > red_max
                        success = false
                        break
                    elsif color == 'green' && val > green_max
                        success = false
                        break
                    elsif color == 'blue' && val > blue_max
                        success = false
                        break
                    end
                end
            end
            if success
                # puts "#{i+1} success"
                count += (i+1)
            end
        end
        return count
    end

    def part_two(input)
        games = parse(input)
        count = 0
        # puts "Game len #{games.length}"
        for i in 0...games.length
            # puts "Game: #{games[i].inspect}"
            game = games[i]
            red_max, green_max, blue_max = nil, nil, nil
            for j in 0...game.length
                # puts "this: #{games[i][j]}"
                move = game[j]
                for k in 0...move.length
                    val, color = move[k]
                    # puts val, color
                    if color == 'red' && (red_max == nil || val > red_max)
                        red_max = val
                    elsif color == 'green' && (green_max == nil || val > green_max)
                        green_max = val
                    elsif color == 'blue' && (blue_max == nil || val > blue_max)
                        blue_max = val
                    end
                end
            end
            # puts red_max, green_max, blue_max
            count += red_max * green_max * blue_max
        end
        return count
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"