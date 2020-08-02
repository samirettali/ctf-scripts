#!/usr/bin/env ruby
require 'digest'

target = 'qmfunq'

i = 0
while i < 1000 do
  s = Random.new(0)
  rand(1000).times {s.rand(5)}
  pass1 = 6.times.map { ('a'..'z').to_a[s.rand(('a'..'z').to_a.size)]}.join
  pass2 = 6.times.map { ('a'..'z').to_a[s.rand(('a'..'z').to_a.size)]}.join
  if pass2 == target
    puts "Found seed: #{i}"
    puts "Admin password: #{pass1}"
    break
  end
  i += 1
end
