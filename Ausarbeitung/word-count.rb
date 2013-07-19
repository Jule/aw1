#!/usr/bin/env ruby

require 'pdf-reader'
require 'pp'

reader = PDF::Reader.new("content.pdf")

$text = ""
reader.pages.each do |page|

  $text = "#{$text} #{page.text}"
end

$text.gsub!("\t", " ")
$text.gsub!("\n", " ")
$text.gsub!(/[^a-zA-Z ]/, "")

while $text.include?("  ")
  $text.gsub!("  ", " ")
end

words = $text.split(" ")

def groupCount(arr)
  arr.group_by { |w| w }
          .map { |k,v| [k, v.count] }
          .sort_by { |e| e[1] }
          .reverse
end

singleWc = groupCount(words)

puts "25 most used words"
pp singleWc[0,25]


bigrams = words[2..words.count].inject([words[0,2]]) do |sum, x|
  sum + [[sum.last.last, x]]
end

puts "\n\n"
puts "25 most used bigrams"
pp groupCount(bigrams)[0,25]


puts "\n\n"
trigrams = words[3..words.count].inject([words[0,3]]) do |sum, x|
  sum + [[sum[-1][-2], sum[-1][-1], x]]
end

puts "25 most used trigrams"
pp groupCount(trigrams)[0,25]
