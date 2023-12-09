class AOCClass
    def hand_freq_v1(hand)
        hand_by_freq = {}
        hand.each_char do |c|
            if !hand_by_freq.key?(c)
                hand_by_freq[c] = 0
            end
            hand_by_freq[c] += 1
        end
        return hand_by_freq
    end

    def hand_freq_v2(hand)
        # puts hand.inspect
        hand_by_freq = hand_freq_v1(hand)
        num_jokers = hand_by_freq['1']

        if num_jokers.nil? || num_jokers == 5
            # puts hand_by_freq.inspect
            return hand_by_freq
        end

        vals_sorted = hand_by_freq.values.sort.reverse! 
        max_freq = hand_by_freq['1'] == vals_sorted[0] ? vals_sorted[1] : vals_sorted[0]

        
        hand_by_freq.each do |k, v|
            if v == max_freq && k != '1'
                hand_by_freq[k] = v + num_jokers
                hand_by_freq.delete('1')
                break
            end
        end
        # puts hand_by_freq.inspect
        
        return hand_by_freq
    end

    def determine_hand_type(hand, ver)
        hand_by_freq = ver == 'v1' ? hand_freq_v1(hand) : hand_freq_v2(hand)
        # hand.each_char do |c|
        #     if !hand_by_freq.key?(c)
        #         hand_by_freq[c] = 0
        #     end
        #     hand_by_freq[c] += 1
        # end
        ranks = hand_by_freq.values.sort.reverse!

        if ranks[0] == 5 # Five of a kind
            rank = 0
        elsif ranks[0] == 4 # Four of a kind
            rank = 1
        elsif ranks[0] == 3 
            if ranks.include?(2) # Full house
                rank = 2
            else # Three of a kind
                rank = 3
            end
        elsif ranks[0] == 2
            if ranks[1] == 2 # Two pairs
                rank = 4
            else # One pair
                rank = 5
            end
        else # High card
            rank = 6
        end

        return rank
    end

    def process_hand(hand, ver)
        hand.gsub! 'A', 'E'
        hand.gsub! 'K', 'D'
        hand.gsub! 'Q', 'C'
        if ver == 'v1' 
            hand.gsub! 'J', 'B' 
        else
            hand.gsub! 'J', '1'
        end
        hand.gsub! 'T', 'A'
        return hand
    end

    def parse(input, ver)
        hands = []
        input.each_line do |line|
            parts = line.split(' ')
            hand = parts[0]
            hand = process_hand(hand, ver)
            hands << [determine_hand_type(hand, ver), hand, parts[1].to_i]
        end
        hands
    end
    
    def part_one(input)
        hands = parse(input, 'v1')
        hands = hands.sort { |a, b| [a[0], b[1]] <=> [b[0], a[1]] }
        # puts hands.inspect
        s = 0
        i = 0
        while i < hands.length
            s += (hands.length - i) * hands[i][2]
            # puts (hands.length - i), hands[i][2]
            # puts 
            i += 1
        end
        return s
    end

    def part_two(input)
        hands = parse(input, 'v2')
        hands = hands.sort { |a, b| [a[0], b[1]] <=> [b[0], a[1]] }
        # puts hands.inspect
        s = 0
        i = 0
        while i < hands.length
            s += (hands.length - i) * hands[i][2]
            # puts (hands.length - i), hands[i][2]
            # puts 
            i += 1
        end
        return s
    end
end

input_file = File.join(File.dirname(__FILE__), "input.txt")
input = File.read(input_file)
AOC = AOCClass.new
puts "Part one: #{AOC.part_one(input)}"
puts "Part two: #{AOC.part_two(input)}"



# part 2 - 251539037 too high
# 251291305 too high
# 251294000 too high
# 249060290 too low
