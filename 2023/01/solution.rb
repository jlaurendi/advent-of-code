class AOCClass
    def part_one(input)
        total = 0
        input.each_line do |line|
            first_num = nil
            last_num = nil
            line.each_char do |c|
                if c.match?(/[[:digit:]]/)
                    num = c.to_i
                    if first_num.nil?
                        first_num = num
                    else 
                        last_num = num
                    end
                end
            end
            
            # Handle the case where there's only one digit in the line
            if last_num.nil?
                last_num = first_num
            end

            total += first_num * 10 + last_num
        end
        return total
    end

    def part_two(input)
        digit_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        total = 0
        input.each_line do |line|
            first_num = nil
            last_num = nil

            i = 0
            while i < line.length
                c = line[i]

                # Handle a digit
                # puts c, i
                if c.match?(/[[:digit:]]/)
                    num = c.to_i
                    if first_num.nil?
                        first_num = num
                    else 
                        last_num = num
                    end
                    
                    i += 1

                # Otherwise see if there's a number word
                else
                    # Could use a trie.. But let's see if we can just brute force it.

                    word = nil
                    digit_words.each do |w, w_val|
                        j = 0
                        found_word = true
                        while j < w.length
                            if line[i + j] != w[j]
                                found_word = false
                                break
                            end
                            j += 1
                        end

                        if found_word
                            if first_num.nil?
                                first_num = w_val
                            else
                                last_num = w_val
                            end
                            break
                        end
                    end
                    i += 1
                end 
            end

            # Handle the case where there's only one digit in the line
            if last_num.nil?
                last_num = first_num
            end

            total += first_num * 10 + last_num
        end

        return total
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"