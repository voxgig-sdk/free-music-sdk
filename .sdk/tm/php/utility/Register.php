<?php
declare(strict_types=1);

// FreeMusic SDK utility registration

require_once __DIR__ . '/../core/UtilityType.php';
require_once __DIR__ . '/Clean.php';
require_once __DIR__ . '/Done.php';
require_once __DIR__ . '/MakeError.php';
require_once __DIR__ . '/FeatureAdd.php';
require_once __DIR__ . '/FeatureHook.php';
require_once __DIR__ . '/FeatureInit.php';
require_once __DIR__ . '/Fetcher.php';
require_once __DIR__ . '/MakeFetchDef.php';
require_once __DIR__ . '/MakeContext.php';
require_once __DIR__ . '/MakeOptions.php';
require_once __DIR__ . '/MakeRequest.php';
require_once __DIR__ . '/MakeResponse.php';
require_once __DIR__ . '/MakeResult.php';
require_once __DIR__ . '/MakePoint.php';
require_once __DIR__ . '/MakeSpec.php';
require_once __DIR__ . '/MakeUrl.php';
require_once __DIR__ . '/Param.php';
require_once __DIR__ . '/PrepareAuth.php';
require_once __DIR__ . '/PrepareBody.php';
require_once __DIR__ . '/PrepareHeaders.php';
require_once __DIR__ . '/PrepareMethod.php';
require_once __DIR__ . '/PrepareParams.php';
require_once __DIR__ . '/PreparePath.php';
require_once __DIR__ . '/PrepareQuery.php';
require_once __DIR__ . '/ResultBasic.php';
require_once __DIR__ . '/ResultBody.php';
require_once __DIR__ . '/ResultHeaders.php';
require_once __DIR__ . '/TransformRequest.php';
require_once __DIR__ . '/TransformResponse.php';

FreeMusicUtility::setRegistrar(function (FreeMusicUtility $u): void {
    $u->clean = [FreeMusicClean::class, 'call'];
    $u->done = [FreeMusicDone::class, 'call'];
    $u->make_error = [FreeMusicMakeError::class, 'call'];
    $u->feature_add = [FreeMusicFeatureAdd::class, 'call'];
    $u->feature_hook = [FreeMusicFeatureHook::class, 'call'];
    $u->feature_init = [FreeMusicFeatureInit::class, 'call'];
    $u->fetcher = [FreeMusicFetcher::class, 'call'];
    $u->make_fetch_def = [FreeMusicMakeFetchDef::class, 'call'];
    $u->make_context = [FreeMusicMakeContext::class, 'call'];
    $u->make_options = [FreeMusicMakeOptions::class, 'call'];
    $u->make_request = [FreeMusicMakeRequest::class, 'call'];
    $u->make_response = [FreeMusicMakeResponse::class, 'call'];
    $u->make_result = [FreeMusicMakeResult::class, 'call'];
    $u->make_point = [FreeMusicMakePoint::class, 'call'];
    $u->make_spec = [FreeMusicMakeSpec::class, 'call'];
    $u->make_url = [FreeMusicMakeUrl::class, 'call'];
    $u->param = [FreeMusicParam::class, 'call'];
    $u->prepare_auth = [FreeMusicPrepareAuth::class, 'call'];
    $u->prepare_body = [FreeMusicPrepareBody::class, 'call'];
    $u->prepare_headers = [FreeMusicPrepareHeaders::class, 'call'];
    $u->prepare_method = [FreeMusicPrepareMethod::class, 'call'];
    $u->prepare_params = [FreeMusicPrepareParams::class, 'call'];
    $u->prepare_path = [FreeMusicPreparePath::class, 'call'];
    $u->prepare_query = [FreeMusicPrepareQuery::class, 'call'];
    $u->result_basic = [FreeMusicResultBasic::class, 'call'];
    $u->result_body = [FreeMusicResultBody::class, 'call'];
    $u->result_headers = [FreeMusicResultHeaders::class, 'call'];
    $u->transform_request = [FreeMusicTransformRequest::class, 'call'];
    $u->transform_response = [FreeMusicTransformResponse::class, 'call'];
});
