create table footballer(
	id_footballer integer  not null,
	name_team char(50),
	name_footballer char(50),
	age integer
);

create table football_team(
	name_team char(50) not null,
	id_league integer,
	coach char(50),
	number_of_players integer,
	stadium char(50)
);

create table football_league(
	id_league integer not null,
	name_league char(50)
);

alter table footballer add constraint pk_footballer primary key (id_footballer);
alter table football_team add constraint pk_football_team primary key (name_team);
alter table football_league add constraint pk_football_league primary key (id_league);

alter table footballer add constraint fk_footballer_team foreign key (name_team) references football_team (name_team);
alter table football_team add constraint fk_team_league foreign key (id_league) references football_league (id_league);