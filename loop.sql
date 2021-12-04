create table footballer_copy as select * from footballer
delete from footballer_copy
select * from footballer_copy
drop table footballer_copy
 
do $$
declare
    foot_id footballer_copy.id_footballer%type;
    general_footballer footballer_copy.name_footballer%type;
begin
    foot_id := 105;
    general_footballer := 'Footballer';
    for counter in 1..15
        loop
            insert into footballer_copy(id_footballer, name_footballer)
            values (foot_id + counter, general_footballer || counter);
        end loop;
end;
$$