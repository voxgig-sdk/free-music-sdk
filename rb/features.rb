# FreeMusic SDK feature factory

require_relative 'feature/base_feature'
require_relative 'feature/ratelimit_feature'
require_relative 'feature/retry_feature'
require_relative 'feature/test_feature'
require_relative 'feature/timeout_feature'


module FreeMusicFeatures
  def self.make_feature(name)
    case name
    when "base"
      FreeMusicBaseFeature.new
    when "ratelimit"
      FreeMusicRatelimitFeature.new
    when "retry"
      FreeMusicRetryFeature.new
    when "test"
      FreeMusicTestFeature.new
    when "timeout"
      FreeMusicTimeoutFeature.new
    else
      FreeMusicBaseFeature.new
    end
  end
end
