#!/usr/bin/env ruby
# puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
ARGV[0].scan(/\[from:(.+)\] \[to:(.+)\] \[flags:((:?\-?\d)+)\]/) { |g_1, g_2, g_3| puts "#{g_1},#{g_2},#{g_3}" }
