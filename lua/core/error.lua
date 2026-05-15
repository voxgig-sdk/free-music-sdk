-- FreeMusic SDK error

local FreeMusicError = {}
FreeMusicError.__index = FreeMusicError


function FreeMusicError.new(code, msg, ctx)
  local self = setmetatable({}, FreeMusicError)
  self.is_sdk_error = true
  self.sdk = "FreeMusic"
  self.code = code or ""
  self.msg = msg or ""
  self.ctx = ctx
  self.result = nil
  self.spec = nil
  return self
end


function FreeMusicError:error()
  return self.msg
end


function FreeMusicError:__tostring()
  return self.msg
end


return FreeMusicError
