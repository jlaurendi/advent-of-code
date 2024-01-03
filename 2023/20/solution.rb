class AOCClass
    ON_STATE = "on"
    OFF_STATE = "off"

    def parse(input)
        @nodes = {}
        lines = input.split("\n")
        node_state = nil
        lines.each do |line|
            parts = line.split(' -> ')
            name = parts[0] == "broadcaster" ? "broadcaster" : parts[0][1..]
            node_type = parts[0][0]
            child_nodes = parts[1].split(', ')
            node_val = 0 if node_type == "%"
            node_state = OFF_STATE if node_type == "%"
            node_state = {} if node_type == "&"
            node = {
                "type": node_type,
                "children": child_nodes,
                "state": node_state
            }
            @nodes[name] = node
        end
        @nodes["button"] = {
            "type": "button", 
            "children": ["broadcaster"]
        }

        @nodes.each do |n1_name, n1|
            if n1[:type] == "&"
                @nodes.each do |n2_name, n2|
                    if n2[:children].include?(n1_name)
                        n1[:state][n2_name] = 0
                    end
                end
            end
        end
    end

    def push_button
        q = [["button", "broadcaster", 0]]
        @low_pulses += 1
        while q.any?
            origin_name, node_name, pulse = q.shift
            pulse_name = (pulse == 0) ? "low" : "high"
            
            # puts "#{origin_name} -#{pulse}-> #{node_name}"
            if @nodes[node_name].nil?
                next
            end

            node = @nodes[node_name]
            if node[:type] == "&"
                node[:state][origin_name] = pulse
                values = node[:state].values
                all_high = values.reduce(true) {|acc, elt| acc && (elt == 1)}
                pulse = all_high ? 0 : 1
            elsif node[:type] == "%"
                if pulse == 0
                    node[:state] = (node[:state] == OFF_STATE) ? ON_STATE : OFF_STATE
                    pulse = (node[:state] == OFF_STATE) ? 0 : 1
                else # high pulse
                    next
                end
            end

            if node_name == "rx"
                puts "rx: "
            end
            

            node[:children].each do |neighbor_name|
                @low_pulses += 1 if pulse == 0
                @high_pulses += 1 if pulse == 1

                q.push([node_name, neighbor_name, pulse])
            end
        end
    end

    def part_one(input)
        parse(input)
        @low_pulses = 0
        @high_pulses = 0
        num_pushes = 1000
        num_pushes.times do |i|
            push_button
        end
        puts "low: #{@low_pulses} high: #{@high_pulses}"
        return @low_pulses * @high_pulses
    end

    def part_two(input)
        return "incomplete"
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"