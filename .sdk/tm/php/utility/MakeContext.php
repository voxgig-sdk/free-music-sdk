<?php
declare(strict_types=1);

// FreeMusic SDK utility: make_context

require_once __DIR__ . '/../core/Context.php';

class FreeMusicMakeContext
{
    public static function call(array $ctxmap, ?FreeMusicContext $basectx): FreeMusicContext
    {
        return new FreeMusicContext($ctxmap, $basectx);
    }
}
