class Directory
    attr_accessor :child_files, :child_directories
    attr_reader :parent, :name

    def initialize(name, parent=nil)
        @name = name
        @parent = parent
        @child_directories = {}
        @child_files = []
    end

    def print
        puts @name
        files_string = @child_files.map{ |f| f.name }.join(" ")
        # puts @child_files.inspect
        puts "Files: #{files_string}"

        child_files_string = @child_directories.map{ |k, v| v.name }.join(" ")
        puts "Children: #{child_files_string}"
        @child_directories.each do |k, d|
            # puts d.inspect
            d.print
        end
    end

    def get_child(name)
        return @child_directories[name]
    end

    def add_child(name, dir)
        @child_directories[name] = dir
    end

    def get_total_size
        files_sum = @child_files.map{ |f| f.size }.sum
        sub_dir_sum = @child_directories.map{ |k,v| v.get_total_size }.sum
        return files_sum + sub_dir_sum
    end

    def get_leaves
        leaves = []
        queue = [self]
        while queue.length > 0
            curr = queue.shift
            if curr.child_directories.length == 0
                leaves.append(curr)
            else
                curr.child_directories.each do |k, dir|
                    queue.append(dir)
                end
            end
        end
        return leaves
    end
end

class File
    attr_accessor :name, :size

    def initialize(name, size)
        @name = name 
        @size = size.to_i
    end
end


class AOCClass
    @curr_dir
    @root_dir
    TOTAL_DISK_SPACE = 70000000
    MIN_SPACE_NEEDED = 30000000


    def parse_command(lines, idx)
        command_and_args = lines[idx][2..].split(" ")
        args = command_and_args[1..]
        command = command_and_args[0]
        
        if command == "cd"
            if args[0] == "/"
                @curr_dir = @root_dir
            elsif args[0] == ".."
                @curr_dir = @curr_dir.parent()
            else
                @curr_dir = @curr_dir.get_child(args[0])
            end    
            idx += 1
        elsif command == "ls"
            while (idx+1) < lines.length && lines[idx+1][0] != "$"
                idx += 1
                line = lines[idx]
                args = line.split(" ")

                if lines[idx].start_with?("dir")
                    dir_name = line.split(" ")[1]
                    new_dir = Directory.new(dir_name, @curr_dir)
                    @curr_dir.add_child(dir_name, new_dir)
                else
                    @curr_dir.child_files.append(File.new(args[1], args[0]))
                end
                    
            end
            idx += 1
        end 

        return idx
    end

    def parse_input(input)
        @root_dir = Directory.new("/")
        @curr_dir = @root_dir

        i = 0
        while i < input.lines.length
            line = input.lines[i].tr("\n", "")
            i = parse_command(input.lines, i)
        end

        return @root_dir
    end

    def part_one(input)
        filesystem = parse_input(input)
        queue = filesystem.get_leaves

        total_size = 0
        while queue.length > 0
            curr = queue.shift
            curr_size = curr.get_total_size
            if curr_size <= 100000
                total_size += curr_size

                unless curr.parent.nil?
                    queue.append(curr.parent)
                end
            end            
        end

        return total_size
    end

    def part_two(input)
        filesystem = parse_input(input)
        curr_disk_space = TOTAL_DISK_SPACE - filesystem.get_total_size
        queue = filesystem.get_leaves
        possible_sizes = []
        while queue.length > 0
            curr = queue.shift
            curr_size = curr.get_total_size
            if (curr_size + curr_disk_space) <= MIN_SPACE_NEEDED
                unless curr.parent.nil?
                    queue.append(curr.parent)
                end
            else
                possible_sizes.append(curr_size)
            end            
        end

        return possible_sizes.min
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
# input = "$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"

#part two
# 37072768 - too high