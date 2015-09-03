require 'travis'

servo = Travis::Repository.find('servo/servo')
build = servo.builds.detect {|build| 
	puts build.id
	build.id == 78508887
}

log = build.jobs.first.log.body

puts log

# http://rubular.com/r/xLvsgjfkZ0
my_match = /((?<filename>\.[a-zA-Z\.\/]*):(?<linenum>\d)+:(?<comment>.+?(?=\.\/|The)))/m.match(log)

puts my_match