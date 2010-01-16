#!/usr/bin/env python
# encoding: utf-8
"""
relations_stoppwords.py - stoppwords from various sources and years of experiments.

File created by Maximillian Dornseif on 2010-01-16.
Copyright (c) 2010 Maximillian Dornseif . Consider it BSD licensed.
"""

# Worte, die ignoeiert werden sollen/können
stoppwords_de = u'''dieses was media com wir mal lassen hudora wenn unseren sie die der sie und http das ist 
in zu den mit auf nicht de oder wir www ein sich es auch bei werden von jpeg sind dem an können net hdimg
eine 150 wenn des im dass aus href als wird uns haben nach man kann einen durch src img zum um shop width 
so height hat 150x150 einem alle unter sein beim wie sollte aber vor einer am \xfcber unsere ohne nur 
sollten unser dann muss immer dieser ihre ganz online nat\xfcrlich finden artnr wieder unserem noch ihrer 
etwas einfach dazu damit zwei zur org mehr keine nehmen hier gibt diese je dies dabei ab aber aber ach 
acht achte achten achter achtes ag alle allein allem allen aller allerdings alles bzw
allgemeinen als als also am an andere anderen andern anders au auch auch auf aus ausser außer ausserdem
außerdem bald bei beide beiden beim bekannt bereits besonders besser besten bin bis bisher bist da dabei
dadurch dafür dagegen daher dahin dahinter damals damit danach daneben dank dann daran darauf daraus darf
darfst darin darüber darum darunter das das dasein daselbst dass daß dasselbe davon davor dazu dazwischen
dein deine deinem deiner dem dementsprechend demgegenüber demgemäss demgemäß demselben demzufolge den
denen denn denn denselben der deren derjenige derjenigen dermassen dermaßen derselbe derselben des deshalb
desselben dessen deswegen d.h dich die diejenige diejenigen dies diese dieselbe dieselben diesem diesen
dieser dieses dir doch dort drei drin dritte dritten dritter drittes du durch durchaus eben ebenso eigen
eigene eigenen eigener eigenes ein einander eine einem einen einer eines einige einigen einiger einiges
einmal einmal eins elf en ende endlich entweder entweder er ernst erst erste ersten erster erstes es etwa
etwas euch früher fünf fünfte fünften fünfter fünftes für gab ganz ganze ganzen ganzer ganzes gar gedurft
gegen gegenüber gehabt gehen geht gekannt gekonnt gemacht gemocht gemusst genug gerade gern gesagt gesagt
geschweige gewesen gewollt geworden gibt ging gleich gott gross groß grosse große grossen großen grosser
großer grosses großes gut gute guter gutes habe haben habt hast hat hatte hätte hatten hätten heisst her
heute hier hin hinter hoch ich ihm ihn ihnen ihr ihre ihrem ihren ihrer ihres im im immer in in indem
infolgedessen ins irgend ist ja ja jahr jahre jahren je jede jedem jeden jeder jedermann jedermanns jedoch
jemand jemandem jemanden jene jenem jenen jener jenes jetzt kam kann kannst kaum kein keine keinem keinen
keiner kleine kleinen kleiner kleines kommen kommt können könnt konnte könnte konnten kurz lang lange
lange leicht leide lieber los machen macht machte mag magst mahn man manche manchem manchen mancher
manches mann mehr mein meine meinem meinen meiner meines mich mir mit mittel mochte möchte mochten mögen
möglich mögt morgen muss muß müssen musst müsst musste mussten na nach nachdem nahm natürlich neben nein
neue neuen neun neunte neunten neunter neuntes nicht nicht nichts nie niemand niemandem niemanden noch nun
nun nur ob oben oder oder offen oft oft ohne recht rechte rechten rechter rechtes richtig rund sa sache
sagt sagte sah satt schon sechs sechste sechsten sechster sechstes sehr sei sei seid seien sein seine
seinem seinen seiner seines seit seitdem selbst selbst sich sie sieben siebente siebenten siebenter
siebentes sind so solang solche solchem solchen solcher solches soll sollen sollte sollten sondern sonst
sowie später statt tat teil tel tritt trotzdem tun über überhaupt übrigens uhr um und und uns unser
unsere unserer unter vergangenen viel viele vielem vielen vielleicht vier vierte vierten vierter viertes
vom von vor während währenddem währenddessen wann war wäre waren wart warum was wegen weil weit
weiter weitere weiteren weiteres welche welchem welchen welcher welches wem wen wenig wenig wenige weniger
weniges wenigstens wenn wenn wer werde werden werdet wessen wie wie wieder will willst wir wird wirklich
wirst wo wohl wollen wollt wollte wollten worden wurde würde wurden würden z.b zehn zehnte zehnten zehnter
zehntes zeit zu zuerst zugleich zum zum zunächst zur zurück zusammen zwanzig zwar zwar zwei zweite zweiten
zweiter zweites zwischen zwölf
aber alle allem allen aller alles also ander andere anderem anderen anderer anderes anderm andern anderr
anders auch bist damit dann derselbe derselben denselben desselben demselben dieselbe dieselben dasselbe
dazu dein deine deinem deinen deiner deines denn derer dessen dich dies diese diesem diesen dieser dieses
doch dort durch eine einem einen einer eines einig einige einigem einigen einiger einiges einmal etwas
euer eure eurem euren eurer eures gegen gewesen habe haben hatte hatten hier hinter mich ihre ihrem ihren
ihrer ihres euch indem jede jedem jeden jeder jedes jene jenem jenen jener jenes jetzt kann kein keine
keinem keinen keiner keines können könnte machen manche manchem manchen mancher manches mein meine
meinem meinen meiner meines muss musste nach nicht nichts noch oder ohne sehr sein seine seinem seinen
seiner seines selbst sich ihnen sind solche solchem solchen solcher solches soll sollte sondern sonst
über unse unsem unsen unser unses unter viel während waren warst weil weiter welche welchem welchen
welcher welches wenn werde werden wieder will wird wirst wollen wollte würde würden zwar zwischen
pictures jpg jpeg png hdimg ror
'''

stoppwords_en = '''i a about an and are as at be by com de en for from how now in is it la of on or that the this
to was what when where who will with und the www you'''




stoppwords = dict([(x, True) for x in (stoppwords_de + stoppwords_en).split()])


