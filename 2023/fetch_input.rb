require "net/http"
require "uri"
require "FileUtils"
session_cookie = ENV["AOC_SESSION_COOKIE"]

if session_cookie.nil?
	raise "Please set AOC_SESSION_COOKIE as an environment variable: export AOC_SESSION_COOKIE=<INSERT-COOKIE>"
end

def fetch_input(year, day, session_cookie)
	year = year.to_i
	day = day.to_i
	raise "Year must be a 4-digit integer greater than 2000" unless year > 2000 and year < 9999
	raise "Day must be a valid integer between 1 and 31" unless (1..31).include?(day.to_i)

	uri = URI.parse("https://adventofcode.com/#{year}/day/#{day}/input")
	http = Net::HTTP.new(uri.host, uri.port)
	http.use_ssl = true
	headers = {
		"Cookie" => "session=#{session_cookie}"
	}
	request = Net::HTTP::Get.new(uri.request_uri, headers)
	response = http.request(request)
	if response.is_a?(Net::HTTPSuccess)
		response.body.strip
	else
		raise "Failed to fetch input: #{response.code} #{response.message}"
	end
end

if __FILE__ == $0
  year = ARGV[0].to_i
  day = ARGV[1].to_i

  # Validate year and day inputs
  if year.nil? || day.nil?
    puts "Usage: ruby fetch_input.rb YEAR DAY"
    exit 1
  end

  input = fetch_input(year, day, session_cookie)
  day_string = (1..9).include?(day) ? "0#{day.to_s}" : day.to_s

 	directory_filename = "#{day_string}"
  input_filename = "#{day_string}/input.txt"

	FileUtils.mkdir_p(directory_filename)
  File.write(input_filename, input)

  solution_filename = "#{day_string}/solution.rb"
  unless File.exist?(solution_filename)
	  FileUtils.cp("template.rb", solution_filename)
  end
end