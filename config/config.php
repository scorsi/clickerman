<?php

/*
 * BASE CONFIG
 */

const DEVELOPMENT_ENVIRONMENT = true; // Do not forget to change it to false on prod.
const DEFAULT_URI = '/minimis/public';
const CACHE_PATH = 'cache/';
const SECRET_KEY = 'd0a7e7997b6d5fcd55f4b5c32611b87cd923e88837b63bf2941ef819dc8ca282';
const COOKIE_SUFFIX = 'minimis_';

/*
 * ROUTES CONFIG
 */

const ROUTES_FILE = 'config/routes.yaml';
const ROUTES_CACHE_ENABLED = true;
const ROUTES_CACHE_FILENAME = 'routes.php';

/*
 * RENDERER CONFIG
 */

const TPL_PATH = 'app/views/';
const ERRORS_TPL_PATH = 'errors/';
const TPL_EXT = 'html';
const RENDERER_SETTINGS = array(
    'checksum' => array(),
    'charset' => 'UTF-8',
    'debug' => false,
    'tpl_dir' => '../' . TPL_PATH,
    'cache_dir' => '../' . CACHE_PATH,
    'tpl_ext' => TPL_EXT,
    'base_url' => DEFAULT_URI,
    'php_enabled' => false,
    'auto_escape' => true,
    'sandbox' => true, // It is highly recommended to activate it.
    'remove_comments' => false,
    'registered_tags' => array()
);

/*
 * DATABASE CONFIG
 */

const DB_DRIVER = 'mysql';
const DB_CONFIG = array(
    'driver'    => DB_DRIVER,
    'host'      => 'localhost',
    'database'  => 'minimis',
    'username'  => 'root',
    'password'  => '',
    'charset'   => 'utf8',
    'collation' => 'utf8_unicode_ci',
    'options'   => array(
        PDO::ATTR_TIMEOUT => 5,
        PDO::ATTR_EMULATE_PREPARES => true,
    )
);