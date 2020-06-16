# Searchepreneurs

Searchepreneurs is a website that allows users to purchase 'SEO audits'. What this means is that, 
after an audit is purchased, an auditor will look through the user's site, as well as use a variety 
of programs (such as load-time checkers) to evaluate how good that site is at search engine 
optimization (SEO).

An auditor will then be able to write a report to the client, informing them of what they need to 
do to optimize their site for search engines. With higher-price audits, the auditor may also take 
their own steps (with the client's permission) to optimize the site, such as generating and 
submitting an XML sitemap.

Searchepreneurs is run off of the Django framework, to allow for authorization, template usage and 
the frictionless creation of url routes, models, templates and functions.

## UX

This website is designed for business owners, where part or all of there business is online. These 
business owners want to improve their site's ranking on search engines such as google.

Searchepreneurs facilitates this, by allowing a user to purchase an 'audit' for their business's 
website. When an audit is purchased, a Searchepreneurs employee will inspect the user's site (both 
visually *and* in google devtools), as well as run it through a website speed tester such as this 
one from [dotcom tools](https://www.dotcom-tools.com/website-speed-test.aspx).

The navbar and footer of the site are a light blue, while the background for the site is white. This 
is to ensure that the site looks professional and has a consistent colour scheme.

In addition, there are four pages on the site relevant to a user's account. These are:
* The 'profile' page
* The 'login' page
* The 'password-reset' page
* The 'register' page

There is also the 'logout' function, which logs a user out.

For simplitity and minimalism, the 'profile' and 'logout' navbar links are only availible if the user 
is already logged in, while the 'login' and 'register' navbar links are only available if the user is 
*not* logged in.

In addition, the 'password-reset' page is only accesible by a link in the 'login' page, as it is 
unlikely that a user would want to reset their password before attempting to log into the site, and 
therefore it is unnecesary to have the link in the navbar.

### User Stories:

#### User Type 1 - Small business owner

* As a small business owner, I want a cheap audit that tells me the basics of what I need to do. I 
don't have a lot of resources, so I want to be given simple ways to optimize my site.

#### User Type 2 - Moderately Large Business owner

* As a moderate business owner, I want a moderately priced audit that will give me ways to optimize 
the site that are within my capabilities. I probably have the basics already optimized for the site 
and so I wish to learn new, less simple ways to optimize.

#### User Type 3 - Large Business owner

* As a large business owner, I am not sensitive to the price of the audit. I want an extensive audit 
that will thoroughly evaluate my site and will provide me with a large number of ways to optimize, 
regardless of their cost.

#### User Type 4 - Mobile User

* As a mobile user, I want to be able to access this site and pay for an audit using my mobile, as well 
as wanting the site to look good on a mobile device, so that I can browse the site and decide on a 
purchase using a mobile phone.

#### User Type 5 - Tablet User

* As a tablet user, I want to be able to access this site and pay for an audit using a tablet, as well 
as wanting the site to look good on a tablet so that I can browse the site and decide on a purchase using 
my tablet.

## Features: