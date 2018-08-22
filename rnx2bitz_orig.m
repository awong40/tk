function navdata = rnx2bitz(rnxFile)
%
% [trackResults] = rnx2bitz(rnxFile)
%
% Description: calculates navigation solutions
%
%   inputs:
%       trackresults    - results from the tracking function (structure
%                       array).
%       settings        - receiver settings.
%   outputs:
%       navsolutions    - contains measured pseudoranges, receiver
%                       clock error, receiver coordinates in several
%                       coordinate systems (at least ecef and utm).
%       eph             - received ephemerides of all sv (structure array).
%
% revision history:
%
% date      programmer     revision description
% ========  ==========     ====================
% 8-8-18    anissa         first cut
%
% (c) copyright 2018, etherwhere inc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
navdata=struct('prn',NaN,'year',NaN,'month',NaN,'day',NaN,'hour',NaN,'minute',NaN,'second',NaN,'a0',NaN,...
'a1',NaN,'a2',NaN,'iode',NaN,'crs',NaN,'deltan',NaN,'M0',NaN,'cuc',NaN,'e',NaN,'cus',NaN,'sqrtA',NaN,'toe',NaN,'cic',...
NaN,'comega',NaN,'cis',NaN,'i0',NaN,'crc',NaN,'omega',NaN,'comegadot',NaN,'idot',NaN,'l2',NaN,'weekNumber',...
NaN,'l2p',NaN,'accuracy',NaN,'health',NaN,'tgd',NaN,'iodc',NaN,'msProcessed',NaN) 
fid=fopen('/home/ec2-user/Documents/new.n','r');
head_lines=0;
while 1
head_lines=head_lines+1;
line=fgetl(fid);
answer=findstr(line,'END OF HEADER');
if~isempty(answer)
break
end
end
noeph=-1;
while 1
noeph=noeph+1;
line=fgetl(fid);
if line==-1
break
end
end
noeph=noeph/8;
frewind(fid);
for l=1:head_lines
line=fgetl(fid);
end
for i=1:noeph
line=fgetl(fid);%first line
navdata(i).prn=str2num(line(1:2));
y=str2num(line(3:6));
if y>79
navdata(i).year=y+1900;
else
navdata(i).year=y+2000;
end
navdata(i).month=str2num(line(7:9));
navdata(i).day=str2num(line(10:12));
navdata(i).hour=str2num(line(13:15));
navdata(i).minute=str2num(line(16:18));
navdata(i).second=str2num(line(19:22));
navdata(i).a0=str2num(line(23:41));
navdata(i).a1=str2num(line(42:60));
navdata(i).a2=str2num(line(61:79));
line=fgetl(fid);%second line
navdata(i).iode=str2num(line(4:22));
navdata(i).crs=str2num(line(23:41));
navdata(i).deltan=str2num(line(42:60));
navdata(i).M0=str2num(line(61:79));
line=fgetl(fid);%third line
navdata(i).cuc=str2num(line(4:22));
navdata(i).e=str2num(line(23:41));
navdata(i).cus=str2num(line(42:60));
navdata(i).sqrtA=str2num(line(61:79)); 
line=fgetl(fid);%fourth line
navdata(i).toe=str2num(line(4:22)); 
navdata(i).cic=str2num(line(23:41)); 
navdata(i).comega=str2num(line(42:60)); 
navdata(i).cis=str2num(line(61:79)); 
line=fgetl(fid);%fifth line
navdata(i).i0=str2num(line(4:22)); 
navdata(i).crc=str2num(line(23:41)); 
navdata(i).omega=str2num(line(42:60)); 
navdata(i).comegadot=str2num(line(61:79)); 
line=fgetl(fid);%sixth linea_f2
navdata(i).idot=str2num(line(4:22)); 
navdata(i).l2=str2num(line(23:41)); 
navdata(i).weekNumber=str2num(line(42:60)); 
navdata(i).l2p=str2num(line(61:79)); 
line=fgetl(fid);%seventh line
navdata(i).accuracy=str2num(line(4:22)); 
navdata(i).health=str2num(line(23:41)); 
navdata(i).tgd=str2num(line(42:60)); 
navdata(i).iodc=str2num(line(61:79)); 
line=fgetl(fid);%eighth line
navdata(i).msProcessed=str2num(line(4:22)); 
end





