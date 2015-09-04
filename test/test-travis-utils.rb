require "minitest/autorun"
require "travis"
require File.expand_path("../../lib/travis-utils", __FILE__)

class TestTravisUtils < Minitest::Test
  def setup
    @build = TravisUtils.get_build_by_id('servo/servo', 78508887)
    @log = TravisUtils.get_log(@build)
  end
  
  def test_get_build_by_id
    assert_instance_of(Travis::Client::Build, @build)
    assert_raises(Travis::Client::NotFound) {TravisUtils.get_build_by_id('bogus/xxx', 00000000)}
  end

  def test_get_log
    assert_instance_of(String, @log)
  end

  def test_parse_log
    data = []
    data.push({
      fname:   "./components/layout/context.rs",
      linenum: "28",
      comment: "use statement is not in alphabetical orderexpected: std::sync::mpsc::{channel, Sender}found: std::sync::{Arc, Mutex, RwLock}"
    })
    data.push({
      fname:   "./components/layout/context.rs",
      linenum: "29",
      comment: "use statement is not in alphabetical orderexpected: std::sync::{Arc, Mutex, RwLock}found: std::sync::mpsc::{channel, Sender}"
    })

    re = /(
           (?<filename>\.[a-zA-Z\.\/]*)
           :(?<linenum>\d+):\s
           (?<comment>.+?(?=\.\/|The|travis))
          )/mx

    assert_equal(data, TravisUtils.parse_log(@log, re))
  end
end