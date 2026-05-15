package core

type FreeMusicError struct {
	IsFreeMusicError bool
	Sdk              string
	Code             string
	Msg              string
	Ctx              *Context
	Result           any
	Spec             any
}

func NewFreeMusicError(code string, msg string, ctx *Context) *FreeMusicError {
	return &FreeMusicError{
		IsFreeMusicError: true,
		Sdk:              "FreeMusic",
		Code:             code,
		Msg:              msg,
		Ctx:              ctx,
	}
}

func (e *FreeMusicError) Error() string {
	return e.Msg
}
