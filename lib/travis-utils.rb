require 'travis'

module TravisUtils

	def TravisUtils.get_build_by_id(repo, build_id)
		repo_actual = Travis::Repository.find(repo)

		build = repo_actual.builds.detect {|build|
			build.id == build_id
		}	
	end

	def TravisUtils.get_log(build)
		build.jobs.first.log.clean_body
	end

	def TravisUtils.parse_log(log, re)
		results = []

		log.scan(re) {|fname,linenum,comment| 
      comment.class
			results.push({
				fname: fname.to_s, 
				linenum: linenum.to_s, 
				comment: comment.delete("\n")
			}) 
		}

    results
	end
end