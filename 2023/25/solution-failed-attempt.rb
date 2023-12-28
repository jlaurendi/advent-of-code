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
        num_components = 0
        visited = {}
        while not_visited.any?
            # puts not_visited.inspect
            node = not_visited.shift
            # next_component = {}
            q = [node]
            while q.any?
                node = q.pop
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
            num_components += 1
        end
        return num_components
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


    def part_one(input)
        parse(input)
        # print_adj
        # puts @v.inspect
        # puts @e.length
        # exit
        # puts "running all pairs shortest path..."
        # input_file = File.join(File.dirname(__FILE__), "apsp.txt")
        # if File.exist?(input_file)
        #     puts "here"
        #     input = File.read(input_file)
        #     e_freq = eval(input)
        #     # puts e_freq.inspect
        #     # exit
        # else
        #     puts "not exist"
        #     e_freq = run_all_pairs_shortest_path
        # end

        # puts "...done"
        # puts e_freq.inspect
        # puts e_freq.inspect
        # exit
        # e_sorted = @e.sort_by {|e| -e_freq[e] }
        # max_edge_len = 14995
        # max_edge =  ["cqn", "pgr"]
        # search = true
        # e_sorted.each do |e|
        #     if search && e !=  ["cqn", "pgr"]
        #         next
        #     elsif search && e == ["cqn", "pgr"]
        #         search = false
        #         next
        #     end
        #     puts "Checking: #{e}"
        #     e_freq2 = run_all_pairs_shortest_path([e])
        #     e_freq2.each do |k,v|
        #         if max_edge.nil? || v > max_edge_len
        #             max_edge = k 
        #             max_edge_len = v 
        #             puts "max edge: #{max_edge} - #{max_edge_len}"
        #         end
        #     end
        # end
        # puts "max edge: #{max_edge} - #{max_edge_len}"
        # exit

        # e_sorted


        connected_components = []
        # try sorting edges by # of shortest paths that go through it?
        found = false
        # top_edges = [["cqn", "pgr"], ["jxz", "zhm"], ["nxd", "ztl"], ["hpv", "xvs"], ["dnk", "frp"], ["fgn", "nrd"], ["fqf", "xzp"], ["cmn", "vfz"], ["mqq", "xrp"], ["jzc", "qsd"], ["gfh", "kps"], ["jjj", "xbz"]]
        # e_sorted_short = [["jxz", "zhm"]]
        @e.each_with_index do |e1, idx1|
            puts "Checking #{e1}"
            # if idx1 > 9
            #     break
            # end
            # puts "running all pairs shortest path #{e1}..."
            # e_freq2 = run_all_pairs_shortest_path([e1])
            # puts e_freq2.inspect
            # exit
            # puts "...done"
            # puts e_freq2.inspect
            # e_sorted2 = @e.sort_by {|e| -e_freq2[e] }
            @e.each_with_index do |e2, idx2|
                if e1 == e2
                    next
                end
                # if idx2 > 99
                #     break
                # end
                # puts "trying #{e2}"
                # puts "running all pairs shortest path #{e1, e2}..."
                # e_freq3 = run_all_pairs_shortest_path([e1, e2])
                # puts "...done"
                # e_sorted3 = @e.sort_by {|e| -e_freq3[e] }
                @e.each_with_index do |e3, idx3|
                    if e2 == e3 || e1 == e3
                        next
                    end
                    # if idx3 > 99
                    #     break
                    # end
                    num_components = get_connected_components([e1, e2, e3])
                    if num_components > 1
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
        # e_sorted.combination(3).each do |excluded_edges|
        #     connected_components = get_connected_components(@adj, @v, excluded_edges)
        #     if connected_components.length > 1
        #         found = true
        #         puts "Excluded edges: #{excluded_edges}"
        #         break
        #     end
        # end
        if found
            puts "components: ", connected_components.inspect
            return connected_components.map {|x| x.length}.reduce(:*)
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
# searched idx1,2,3 <= 4

# only check shortest path of v1 v2 (e1)