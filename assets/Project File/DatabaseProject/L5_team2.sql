----create database L5_team2_DB

use L5_team2_DB

----OWNER
--create table Owner_info
--(
--owner_id varchar(5) not null,
--owner_name varchar(50)not null,
--contact_info char(8) not null,
--DOB date not null,
--primary key(owner_id)
--);

--bulk insert owner_info
--from 'C:\Users\ollev\Downloads\Owner.txt'

----MANAGER
--create table Manager_info
--(
--manager_id varchar(5) not null,
--contact_info char(8) not null,
--manager_name varchar(50) not null,
--DOB date not null,
--primary key(manager_id)
--);

--bulk insert manager_info
--from 'C:\Users\ollev\Downloads\Manager_info.txt'

----FAN
--create table Fan_info
--(
--fan_id varchar(5) not null,
--DOB date not null,
--fan_name varchar(50),
--gender char(1),
--contact_info char(8) not null,
--primary key(fan_id)
--);

--bulk insert fan_info
--from 'C:\Users\ollev\Downloads\Fan_info.txt'

--PLAYER
--create table Player_info
--(
--player_id varchar(5) not null,
--player_name varchar(50) not null,
--DOB date not null,
--gender char(1),
--contact_info char(8) not null,
--primary key(player_id)
--);

--bulk insert player_info
--from 'C:\Users\ollev\Downloads\Player_info.txt'

----STADIUM
--create table stadiuminfo
--(
--stadium_id varchar(4) not null,
--stadium_name varchar(50) not null,
--address varchar(50),
--primary key(stadium_id)
--); 

--bulk insert stadiuminfo
--from 'C:\Users\ollev\Downloads\Stadium_info.txt'

----PLAYER POSITION
--create table player_position
--(
--position_name varchar(50),
--player_id varchar(5),
--primary key(position_name, player_id),
--foreign key (player_id) references player_info (player_id)
--);

--bulk insert player_position
--from 'C:\Users\ollev\Downloads\Player_positions.txt'

----CLUB INFO
--create table Clubinfo
--(
--club_id varchar(5) not null,
--club_name varchar(50),
--mascot varchar(50),
--stadium_id varchar(5) not null,
--owner_id varchar(5) not null,
--primary key(club_id),
--foreign key (stadium_id) references stadium_info (stadium_id),
--foreign key (owner_id) references owner_info (owner_id)
--);

--bulk insert clubinfo
--from 'C:\Users\ollev\Downloads\Club_info.txt'

----MEMBERSHIP INFO
--create table membership_info
--(
--member_id varchar(5) not null,
--club_id varchar(5) not null,
--fan_id varchar(5) not null,
--start_date date,
--end_date date,
--membership_fee numeric(9,2),
--primary key(member_id),
--foreign key (club_id) references clubinfo (club_id),
--foreign key (fan_id) references fan_info (fan_id)
--);

--bulk insert membership_info
--from 'C:\Users\ollev\Downloads\Membership_info.txt'

----MANAGER CONTRACT
--create table manager_contract
--(
--mcontract_id varchar(5) not null,
--manager_id varchar(5) not null,
--annual_manager_salary numeric(9,2),
--start_date date,
--end_date date,
--club_id varchar(5) not null,
--primary key(mcontract_id),
--foreign key (club_id) references clubinfo (club_id),
--foreign key (manager_id) references manager_info (manager_id)
--);

--bulk insert manager_contract
--from 'C:\Users\ollev\Downloads\manager_contract.txt'

----PLAYER CONTRACT
--create table player_contract
--(
--player_contract_id varchar(5) not null,
--player_id varchar(5) not null,
--jersey_number varchar(2) not null,
--annual_player_salary numeric(9,2),
--start_date date,
--end_date date,
--club_id varchar(5) not null,
--primary key(player_contract_id),
--foreign key (club_id) references clubinfo (club_id),
--foreign key (player_id) references player_info (player_id)
--);

--bulk insert player_contract
--from 'C:\Users\ollev\Downloads\player_contract.txt'

----MATCH INFO
--create table matchinfo
--(
--match_id varchar(4) not null,
--home_team varchar(5) not null,
--away_team varchar(5) not null,
--match_date datetime not null,
--home_score int not null, 
--away_score int not null, 
--stadium_id varchar(5) not null,
--adult_ticket numeric(9,2),
--children_ticket numeric(9,2),
--fan_ticket numeric(9,2),
--game_type varchar(50),
--season_year varchar(50),
--primary key(match_id),
--foreign key (home_team) references clubinfo (club_id),
--foreign key (away_team) references clubinfo (club_id),
--foreign key (stadium_id) references stadium_info (stadium_id),
--);

--bulk insert matchinfo
--from 'C:\Users\ollev\Downloads\match_info.txt'

--TROPHY INFO
--create table trophy_info
--(
--trophy_id varchar(4) not null,
--match_id varchar(4) not null,
--trophy_name varchar(50),
--club_id varchar(5) not null,
--primary key(trophy_id),
--foreign key (match_id) references matchinfo (match_id),
--foreign key (club_id) references clubinfo (club_id),
--);

--bulk insert trophy_info
--from 'C:\Users\ollev\Downloads\trophy_info.txt'

----SUB INFO
--create table substitution_info
--(
--sub_id varchar(6) not null,
--match_id varchar(4) not null,
--out_player_id varchar(5) not null,
--in_player_id varchar(5) not null,
--min_of_change int,
--sub_reason varchar(50),
--primary key(sub_id),
--foreign key (match_id) references matchinfo (match_id),
--foreign key (out_player_id) references player_info (player_id),
--foreign key (in_player_id) references player_info (player_id)
--);

--bulk insert substitution_info
--from 'C:\Users\ollev\Downloads\sub_info.txt'

----GOAL INFO
--create table goal_info
--(
--goal_id varchar(6) not null,
--match_id varchar(4) not null,
--player_id varchar(5) not null,
--time_scored datetime,
--goal_description varchar(50),
--primary key(goal_id),
--foreign key (match_id) references matchinfo (match_id),
--foreign key (player_id) references player_info (player_id) 
--);

--bulk insert goal_info
--from 'C:\Users\ollev\Downloads\goal_info.txt'

--players involved
--create table players_involved
--(
--match_id varchar(4) not null,
--player_id varchar(5) not null,
--representing varchar(10)
--primary key(match_id,player_id),
--foreign key (match_id) references matchinfo (match_id),
--foreign key (player_id) references player_info (player_id) 
--);

--bulk insert players_involved
--from 'C:\Users\ollev\Downloads\players_involved.txt'

--select * from owner_info
--select * from manager_info
--select * from fan_info
--select * from player_info
--select * from stadium_info
--select * from player_position
--select * from clubinfo
--select * from membership_info
--select * from manager_contract
--select * from player_contract
--select * from matchinfo
--select * from trophy_info
--select * from substitution_info
--select * from goal_info


----14.1
--select start_date, sum(membership_fee) as "Total membership fee"
--from membership_info
--where year(start_date) in ('2023','2024')
--group by start_date

----14.2
--select c.club_name, p.player_name, count(pp.position_name) as "Number of positions"
--from player_info as p
--inner join player_position as pp on pp.player_id = p.player_id
--inner join player_contract as pc on pc.player_id = p.player_id
--inner join club_info as c  on c.club_id   = pc.club_id
--group by c.club_name, p.player_id, p.player_name
--having count(pp.position_name) >= 2
--order by c.club_name, "Number of positions" desc, p.player_name;


----14.3
--select
--m.match_id, m.match_date, hc.Club_name as home_team, m.home_score, ac.Club_name as away_team, m.away_score, p.Player_id, p.player_Name as player_name, i.representing,  
--(select count(*)
--from goal_info as g
--where g.match_id = m.match_id
--and g.player_id = p.Player_id) as goals_scored
--from matchinfo as m
--inner join clubinfo as hc on hc.club_id = m.home_team
--inner join clubinfo as ac on ac.club_id = m.away_team
--inner join players_involved as i  on i.match_id = m.match_id
--inner join Player_info as p on p.Player_id = i.player_id
--where m.match_date >= '2024-01-01' and m.match_date <  '2025-01-01'
--and (
--(hc.club_name like 'Liverpool%' and ac.club_name like 'Manchester City%')
--or (hc.club_name like 'Manchester City%' and ac.club_name like 'Liverpool%')
--)
--order by i.representing, p.player_name;

----14.4
--select * from matchinfo 
--where ((home_score-away_score) >=3 or (away_score-home_score) >=3)
--and year(match_date) between 2023 and 2024

--14.5
--select club_id, manager_id, start_date
--from manager_contract
--where year(start_date) between 2019 and 2023