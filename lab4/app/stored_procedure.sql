use lab4;

drop procedure if exists get_shops_after_client;
drop procedure if exists get_terminals_after_shop;
drop procedure if exists get_terminals_after_manufacturer;
drop procedure if exists get_service_jobs_after_service_type;
drop procedure if exists get_masters_after_service_jobs;
drop procedure if exists get_service_job_after_masters;
delimiter ///

create procedure get_shops_after_client(
	in client_id int
    )
begin
	select c.id as client_id, s.id as shop_id, c.name
	from shop s
	join client c on s.client_id = c.id
	where s.client_id = client_id;
end ///

create procedure get_terminals_after_shop(
	in shop_id int
	)
begin
	select shop_id, id as terminal_id
    from terminal
    where terminal.shop_id = shop_id;
end ///

create procedure get_terminals_after_manufacturer(
	in manufactures_id int
    )
begin
	select m.id as manufactures_id, t.id as terminal_id, m.name
	from terminal t
	join manufactures m on t.manufactures_id = m.id
	where t.manufactures_id = manufactures_id;
end ///

create procedure get_service_jobs_after_service_type(
	in service_type_id int
	)
begin
	select st.id as service_type_id, sj.id as service_job_id, st.name
	from service_job sj
	join service_type st on sj.service_type_id = st.id
	where sj.service_type_id = service_type_id;
end ///

create procedure get_masters_after_service_jobs(
	in service_jod_id int
    )
begin
	select sjm.service_job_id, m.id, m.surname, m.phone_number
	from masters m
	join service_job_masters sjm on m.id = sjm.master_id
	where sjm.service_job_id = service_jod_id;
end ///

create procedure get_service_job_after_masters(
	in master_id int
    )
begin
	select sjm.id, sjm.service_job_id, sj.service_type_id
	from service_job sj
	join service_job_masters sjm on sj.id = sjm.master_id
	where sjm.service_job_id = master_id;
end ///

delimiter ;