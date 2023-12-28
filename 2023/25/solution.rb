require 'json'
class AOCClass
    def parse(input)
        lines = input.split("\n")
        @adj = {}
        @v = []
        @e = []
        lines.each do |line|
            v1, adj = line.split(": ")
            adj = adj.split(" ")
            adj.each do |v2|
                add_to_adj(v1, v2)
                add_to_v(v1)
                add_to_v(v2)
                add_to_e([v1, v2])
            end 
        end
    end

    def add_to_v(v1)
        if !@v.include?(v1)
            @v.append(v1)
        end
    end

    def add_to_e(e)
        @e.push(e.sort)
    end

    def add_to_adj(v1, v2)
        if !@adj.key?(v1)
            @adj[v1] = []
        end
        if !@adj.key?(v2)
            @adj[v2] = []
        end
        @adj[v1].append(v2)
        @adj[v2].append(v1)
    end

    def get_connected_components(excluded_edges = nil)
        not_visited = Marshal.load(Marshal.dump(@v))
        # connected_components = []
        components = []
        visited = {}
        while not_visited.any?
            # puts not_visited.inspect
            node = not_visited.shift
            # next_component = {}
            q = [node]
            num_nodes = 0
            while q.any?
                node = q.pop
                if !visited.key? node
                    num_nodes += 1
                end

                not_visited.delete(node)
                visited[node] = true
                # if !next_component.key?(node)
                #     next_component[node] = true
                # end

                @adj[node].each do |neighbor|
                    exclude = excluded_edges.include?([node, neighbor].sort)
                    if visited[neighbor] || exclude
                        next 
                    end    
                    q.push(neighbor)
                    # visited[neighbor] = true
                    not_visited.delete(neighbor)
                end
            end
            # connected_components.push(next_component)
            components.push(num_nodes)
        end
        return components
    end

    def print_adj
        @adj.each do |k, v|
            puts "#{k}:, #{v}"
        end
    end

    def run_all_pairs_shortest_path(exclude = nil)
        e_freq = {}
        if !exclude.nil?
            exclude.each { |e| e_freq[e] = 0 }
        end
        @v.each do |vert|
            q = [[vert, 0]]
            visited = {}
            while q.any?
                node, l = q.shift
                visited[node] = true
                @adj[node].each do |neighbor|
                    e = [node, neighbor].sort
                    if visited[neighbor] || (exclude != nil && exclude.include?(e))
                        next
                    end
                    q.push([neighbor, l+1])

                    # puts "e: #{e}"
                    if !e_freq.key?(e)
                        e_freq[e] = 0
                    end 
                    # if l > 12
                    e_freq[e] += 1
                    # end
                end
            end
        end
        return e_freq
    end

    def get_edges_on_shortest_path(v1, v2, exclude = nil)
        edges = []
        visited = {}
        q = [[v1]]
        visited[v1] = true
        while q.any?
            nxt = q.shift
            # puts "exploring #{nxt.inspect}"
            @adj[nxt[-1]].each do |neighbor|
                # puts "neighbor: #{neighbor}"
                if visited[neighbor] || (!exclude.nil? && exclude.include?([nxt[-1], neighbor].sort))
                    next
                end
                visited[neighbor] = true
                if neighbor == v2
                    # puts "found!"
                    # puts nxt.inspect
                    nxt.push(neighbor)
                    nxt.each_with_index do |n, i|
                        if i + 1 == nxt.length
                            break
                        end
                        edges |= [[n, nxt[i+1]].sort]
                    end
                    next
                end
                # puts "#{nxt}, #{neighbor}, #{nxt + [neighbor]}"
                q.push(nxt + [neighbor])
            end
        end
        return edges
    end


    def part_one(input)
        parse(input)
        components = []
        found = false
        @e.each_with_index do |e1, idx1|
            puts "Checking #{e1}"
            edges_on_shortest_path1 = get_edges_on_shortest_path(e1[0], e1[1], [e1])
            puts "edges: #{edges_on_shortest_path1.inspect}"
            # exit
            edges_on_shortest_path1.each_with_index do |e2, idx2|
                if e1 == e2
                    next
                end
                edges_on_shortest_path2 = get_edges_on_shortest_path(e2[0], e2[1], [e1, e2])
                edges_on_shortest_path2.each_with_index do |e3, idx3|
                    if e2 == e3 || e1 == e3
                        next
                    end
                    components = get_connected_components([e1, e2, e3])
                    if components.length > 1
                        found = true
                        puts "Excluded edges: #{[e1, e2, e3]}"
                        break
                    end
                end
                if found
                    break
                end
            end
            if found
                break
            end
        end
        if found
            puts "components: ", components.inspect
            return components.reduce(:*)
        else 
            return "not found"
        end
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

# 1481 verts, 3304 edges

# only check shortest path of v1 v2 (e1)