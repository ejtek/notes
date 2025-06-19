
[Source](http://www.petefreitag.com/cheatsheets/apache/ "Permalink to Apache Cheat Sheet")

# Apache

```
In Arch Linux, Apache configuration files are located in `/etc/httpd/conf`. The main configuration file is `/etc/httpd/conf/httpd.conf`, which includes various other configuration files. The default configuration file should be fine for a simple setup. By default, it will serve the directory `/srv/http` to anyone who visits your website.
```
## Setup a Virtual Domain

    NameVirtualHost *
    
      DocumentRoot /web/example.com/www
      ServerName www.example.com
      _ServerAlias example.com
      CustomLog /web/example.com/logs/access.log combined
      ErrorLog /web/example.com/logs/error.log_
    

## Include another conf file

    Include /etc/apache/virtual-hosts/*.conf

## Hide apache version info

    ServerSignature Off
    ServerTokens Prod

## Custom 404 Error message

    ErrorDocument 404 /404.html

## Create a virtual directory (mod_alias)

    Alias /common /web/common

## Perminant redirect (mod_alias)

    Redirect permanent /old http://example.com/new

## Create a cgi-bin

    ScriptAlias /cgi-bin/ /web/cgi-bin/

## Process .cgi scripts

    AddHandler cgi-script .cgi

## Add a directory index

    DirectoryIndex index.cfm index.cfm

## Turn off directory browsing

    Options -Indexes

## Turn on directory browsing

    
      Options +Indexes
    

## Create a new user for basic auth _(command line)_

    htpasswd -c /etc/apacheusers

## Apache basic authentication

    AuthName "Authentication Required"
    AuthType Basic
    AuthUserFile /etc/apacheusers
    Require valid-user

## Only allow access from a specific IP

    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1

## Only allow access from your subnet

    Order Deny,Allow
    Deny from all
    Allow from 176.16.0.0/16

**mod_rewrite**

## Turn on the rewrite engine

    RewriteEngine On

## Redirect /news/123 to /news.cfm?id=123

    RewriteRule ^/news/([0-9]+)$ /news.cfm?id=$1 [PT,L]

## Redirect www.example.com to example.com

    RewriteCond %{HTTP_HOST} ^www.example.com$ [NC]
    RewriteRule ^(.*)$ http://example.com$1 [R=301,L]

_This is a work in progress - Questions, comments, criticism, or requests can be directed [Here][1]_

[More Cheat Sheets Here][2].

_Copyright © 2005 [Peter Freitag][3] (http://www.petefreitag.com/), All Rights Reserved.  
This document may be printed freely as long as this notice stays intact._

[1]: /contact/
[2]: /cheatsheets/
[3]: http://www.petefreitag.com/
