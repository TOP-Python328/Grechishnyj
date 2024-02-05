
-- 1. Вывести названия всех стран Евразии
select name from country
where continent like '%Europe%' 
or continent like '%Asia%' 
order by name;
-- +-------------------------------+
-- | name                          |
-- +-------------------------------+
-- | Afghanistan                   |
-- | Albania                       |
-- | Andorra                       |
-- | Armenia                       |
-- | Austria                       |
-- | Azerbaijan                    |
-- | Bahrain                       |
-- | Bangladesh                    |
-- | Belarus                       |
-- | Belgium                       |
-- | Bhutan                        |
-- | Bosnia and Herzegovina        |
-- | Brunei                        |
-- | Bulgaria                      |
-- | Cambodia                      |
-- | China                         |
-- | Croatia                       |
-- | Cyprus                        |
-- | Czech Republic                |
-- | Denmark                       |
-- | East Timor                    |
-- | Estonia                       |
-- | Faroe Islands                 |
-- | Finland                       |
-- | France                        |
-- | Georgia                       |
-- | Germany                       |
-- | Gibraltar                     |
-- | Greece                        |
-- | Holy See (Vatican City State) |
-- | Hong Kong                     |
-- | Hungary                       |
-- | Iceland                       |
-- | India                         |
-- | Indonesia                     |
-- | Iran                          |
-- | Iraq                          |
-- | Ireland                       |
-- | Israel                        |
-- | Italy                         |
-- | Japan                         |
-- | Jordan                        |
-- | Kazakstan                     |
-- | Kuwait                        |
-- | Kyrgyzstan                    |
-- | Laos                          |
-- | Latvia                        |
-- | Lebanon                       |
-- | Liechtenstein                 |
-- | Lithuania                     |
-- | Luxembourg                    |
-- | Macao                         |
-- | Macedonia                     |
-- | Malaysia                      |
-- | Maldives                      |
-- | Malta                         |
-- | Moldova                       |
-- | Monaco                        |
-- | Mongolia                      |
-- | Myanmar                       |
-- | Nepal                         |
-- | Netherlands                   |
-- | North Korea                   |
-- | Norway                        |
-- | Oman                          |
-- | Pakistan                      |
-- | Palestine                     |
-- | Philippines                   |
-- | Poland                        |
-- | Portugal                      |
-- | Qatar                         |
-- | Romania                       |
-- | Russian Federation            |
-- | San Marino                    |
-- | Saudi Arabia                  |
-- | Singapore                     |
-- | Slovakia                      |
-- | Slovenia                      |
-- | South Korea                   |
-- | Spain                         |
-- | Sri Lanka                     |
-- | Svalbard and Jan Mayen        |
-- | Sweden                        |
-- | Switzerland                   |
-- | Syria                         |
-- | Taiwan                        |
-- | Tajikistan                    |
-- | Thailand                      |
-- | Turkey                        |
-- | Turkmenistan                  |
-- | Ukraine                       |
-- | United Arab Emirates          |
-- | United Kingdom                |
-- | Uzbekistan                    |
-- | Vietnam                       |
-- | Yemen                         |
-- | Yugoslavia                    |
-- +-------------------------------+
-- 97 rows in set (0.0008 sec)


-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select region, name 
from country 
where life_expectancy < 50 
order by region;
-- +---------------------------+---------------------------------------+
-- | region                    | name                                  |
-- +---------------------------+---------------------------------------+
-- | Caribbean                 | Haiti                                 |
-- | Central Africa            | Angola                                |
-- | Central Africa            | Central African Republic              |
-- | Central Africa            | Congo, The Democratic Republic of the |
-- | Central Africa            | Congo                                 |
-- | Eastern Africa            | Burundi                               |
-- | Eastern Africa            | Ethiopia                              |
-- | Eastern Africa            | Kenya                                 |
-- | Eastern Africa            | Mozambique                            |
-- | Eastern Africa            | Malawi                                |
-- | Eastern Africa            | Rwanda                                |
-- | Eastern Africa            | Somalia                               |
-- | Eastern Africa            | Uganda                                |
-- | Eastern Africa            | Zambia                                |
-- | Eastern Africa            | Zimbabwe                              |
-- | Northern Africa           | Western Sahara                        |
-- | Southeast Asia            | East Timor                            |
-- | Southern Africa           | Botswana                              |
-- | Southern Africa           | Namibia                               |
-- | Southern Africa           | Swaziland                             |
-- | Southern and Central Asia | Afghanistan                           |
-- | Western Africa            | Burkina Faso                          |
-- | Western Africa            | Côte d’Ivoire                         |
-- | Western Africa            | Guinea                                |
-- | Western Africa            | Guinea-Bissau                         |
-- | Western Africa            | Mali                                  |
-- | Western Africa            | Niger                                 |
-- | Western Africa            | Sierra Leone                          |
-- +---------------------------+---------------------------------------+
-- 28 rows in set (0.0007 sec)


-- 3. Вывести название самой крупной по площади страны Африки
select name from country 
where region like '%Africa%' 
order by surface_area desc limit 1;

-- +-------+
-- | name  |
-- +-------+
-- | Sudan |
-- +-------+
-- 1 row in set (0.0007 sec)


-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
select name from country 
where continent like '%Asia%' 
order by population / surface_area asc 
limit 5;
-- +--------------+
-- | name         |
-- +--------------+
-- | Mongolia     |
-- | Kazakstan    |
-- | Oman         |
-- | Turkmenistan |
-- | Saudi Arabia |
-- +--------------+
-- 5 rows in set (0.0008 sec)


-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
select country_code, name from city 
where population > 5000000 
order by population;
-- +--------------+-------------------+
-- | country_code | name              |
-- +--------------+-------------------+
-- | PAK          | Lahore            |
-- | COD          | Kinshasa          |
-- | CHN          | Tianjin           |
-- | BRA          | Rio de Janeiro    |
-- | COL          | Santafé de Bogotá |
-- | THA          | Bangkok           |
-- | CHN          | Chongqing         |
-- | PER          | Lima              |
-- | IRN          | Teheran           |
-- | EGY          | Cairo             |
-- | IND          | Delhi             |
-- | GBR          | London            |
-- | CHN          | Peking            |
-- | JPN          | Tokyo             |
-- | USA          | New York          |
-- | RUS          | Moscow            |
-- | MEX          | Ciudad de México  |
-- | TUR          | Istanbul          |
-- | PAK          | Karachi           |
-- | IDN          | Jakarta           |
-- | CHN          | Shanghai          |
-- | BRA          | São Paulo         |
-- | KOR          | Seoul             |
-- | IND          | Mumbai (Bombay)   |
-- +--------------+-------------------+
-- 24 rows in set (0.0019 sec)

-- 6. Вывести название города в Индии с самым длинным названием для подсчёта количества символов используйте встроенную функцию char_length()
select name from city 
where country_code = 'IND' 
order by char_length(name) desc 
limit 1;
-- +--------------------------------+
-- | name                           |
-- +--------------------------------+
-- | Thiruvananthapuram (Trivandrum |
-- +--------------------------------+
-- 1 row in set (0.0019 sec)