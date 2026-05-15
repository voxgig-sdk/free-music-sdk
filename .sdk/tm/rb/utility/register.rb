# FreeMusic SDK utility registration
require_relative '../core/utility_type'
require_relative 'clean'
require_relative 'done'
require_relative 'make_error'
require_relative 'feature_add'
require_relative 'feature_hook'
require_relative 'feature_init'
require_relative 'fetcher'
require_relative 'make_fetch_def'
require_relative 'make_context'
require_relative 'make_options'
require_relative 'make_request'
require_relative 'make_response'
require_relative 'make_result'
require_relative 'make_point'
require_relative 'make_spec'
require_relative 'make_url'
require_relative 'param'
require_relative 'prepare_auth'
require_relative 'prepare_body'
require_relative 'prepare_headers'
require_relative 'prepare_method'
require_relative 'prepare_params'
require_relative 'prepare_path'
require_relative 'prepare_query'
require_relative 'result_basic'
require_relative 'result_body'
require_relative 'result_headers'
require_relative 'transform_request'
require_relative 'transform_response'

FreeMusicUtility.registrar = ->(u) {
  u.clean = FreeMusicUtilities::Clean
  u.done = FreeMusicUtilities::Done
  u.make_error = FreeMusicUtilities::MakeError
  u.feature_add = FreeMusicUtilities::FeatureAdd
  u.feature_hook = FreeMusicUtilities::FeatureHook
  u.feature_init = FreeMusicUtilities::FeatureInit
  u.fetcher = FreeMusicUtilities::Fetcher
  u.make_fetch_def = FreeMusicUtilities::MakeFetchDef
  u.make_context = FreeMusicUtilities::MakeContext
  u.make_options = FreeMusicUtilities::MakeOptions
  u.make_request = FreeMusicUtilities::MakeRequest
  u.make_response = FreeMusicUtilities::MakeResponse
  u.make_result = FreeMusicUtilities::MakeResult
  u.make_point = FreeMusicUtilities::MakePoint
  u.make_spec = FreeMusicUtilities::MakeSpec
  u.make_url = FreeMusicUtilities::MakeUrl
  u.param = FreeMusicUtilities::Param
  u.prepare_auth = FreeMusicUtilities::PrepareAuth
  u.prepare_body = FreeMusicUtilities::PrepareBody
  u.prepare_headers = FreeMusicUtilities::PrepareHeaders
  u.prepare_method = FreeMusicUtilities::PrepareMethod
  u.prepare_params = FreeMusicUtilities::PrepareParams
  u.prepare_path = FreeMusicUtilities::PreparePath
  u.prepare_query = FreeMusicUtilities::PrepareQuery
  u.result_basic = FreeMusicUtilities::ResultBasic
  u.result_body = FreeMusicUtilities::ResultBody
  u.result_headers = FreeMusicUtilities::ResultHeaders
  u.transform_request = FreeMusicUtilities::TransformRequest
  u.transform_response = FreeMusicUtilities::TransformResponse
}
