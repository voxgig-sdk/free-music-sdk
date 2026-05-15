<?php
declare(strict_types=1);

// FreeMusic SDK feature factory

require_once __DIR__ . '/feature/BaseFeature.php';
require_once __DIR__ . '/feature/TestFeature.php';


class FreeMusicFeatures
{
    public static function make_feature(string $name)
    {
        switch ($name) {
            case "base":
                return new FreeMusicBaseFeature();
            case "test":
                return new FreeMusicTestFeature();
            default:
                return new FreeMusicBaseFeature();
        }
    }
}
