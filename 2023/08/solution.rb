class AOCClass
    def parse_map(lines)
        map = {}
        lines.each do |line|
            parts = line.split(' = ')
            p0 = parts[0]
            p1 = parts[1][1..3]
            p2 = parts[1][6..8]
            map[p0] = [p1, p2]
        end
        return map
    end

    def part_one(input)
        lines = input.lines
        instructions = lines[0].strip
        lines.shift(2)
        map = parse_map(lines)

        steps = 0
        i = 0
        curr = "AAA"
        while true
            steps += 1
            instr = instructions[i]
            if instr == "L"
                curr = map[curr][0]
            else
                curr = map[curr][1]
            end

            if curr == "ZZZ"
                break
            end
            i = (i + 1) % instructions.length
        end
        return steps
    end

    def find_starting_nodes(map)
        nodes = []
        map.each do |k,v|
            if k[2] == "A"
                nodes.push(k)
            end
        end
        return nodes
    end

    def part_two(input)
        lines = input.lines
        instructions = lines[0].strip
        lines.shift(2)
        map = parse_map(lines)

        steps = 0
        nodes = find_starting_nodes(map)
        node_cycles = Array.new(nodes.length) { nil }
        num_node_cycles_found = 0
        i = 0
        while true
            steps += 1
            instr = instructions[i]

            all_z = true
            # puts nodes.inspect
            # puts map.inspect
            # puts node_cycles.inspect
            nodes.each_with_index.map do |n, j|
                # puts n, map[n], instr
                # puts
                if instr == "L"
                    new_n = map[n][0]
                else
                    new_n = map[n][1]
                end

                # puts new_n
                if new_n[2] == "Z"
                    # puts j, node_cycles.inspect, num_node_cycles_found
                    if node_cycles[j].nil?
                        node_cycles[j] = steps
                        num_node_cycles_found += 1
                        if num_node_cycles_found == node_cycles.length
                            break
                        end
                    end
                else 
                    all_z = false
                end
                nodes[j] = new_n
            end

            if num_node_cycles_found == node_cycles.length
                break
            end

            i = (i + 1) % instructions.length
        end
        return node_cycles.reduce(1, :lcm)
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
# puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"