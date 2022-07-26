#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+\d+)\] \[to:(\+\d+)\] \[flags:((:{0,1}\-{0,1}\d)+)\]/) { |g_1, g_2, g_2| puts "#{g_1},#{g_2},#{g_2}" }
