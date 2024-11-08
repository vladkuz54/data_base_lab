use lab4;

insert into lab4.client (name) values
("Близенько"),
("Свій маркет"),
("Сім 23"),
("АТБ"),
("Сільпо"),
("Крамничка"),
("Арсен"),
("Ашан"),
("Eva"),
("Фотохата"),
("Піцерія");

insert into lab4.shop_adress (street, street_number, gps_longitude, gps_latitude) values
("вулиця Тараса Шевченка", 1, 40.384922, 35.078145),
("вулиця Степана Бандери", 67, 39.978375, 37.964924),
("проспект Свободи", 4, 40.133424, 40.546249),
("вулиця Богдана Хмельницького", 41, 40.139472, 37.349244),
("вулиця Стрийська", 100, 36.345255, 31.562967),
("проспект Свободи", 2, 41.902452, 32.572923),
("вулиця Тараса Шевченка", 23, 38.112753, 34.748240),
("вулиця Богдана Хмельницького", 7, 40.453453, 37.349244),
("вулиця Стрийська", 67, 40.453143, 37.349267),
("вулиця Зелена", 90, 40.453453, 37.349212),
("вулиця Степана Бандери", 15, 40.459053, 37.349290),
("вулиця Тараса Шевченка", 38, 40.453753, 37.349232);

insert into lab4.shop (client_id, shop_adress_id) values
(3, 1),
(5, 2),
(2, 3),
(11, 4),
(10, 5),
(8, 6),
(10, 7),
(6, 8),
(8, 9),
(6, 10),
(9, 11),
(4, 12);


insert into lab4.service_type (name) values
("Звичайне обсуговування"),
("Капітальний ремонт"),
("Забирання готівки"),
("Оновлення ПО"),
("Заміна клавіатури"),
("Заміна екрану"),
("Виправлення помилки №12"),
("Ремонт датчика NFC"),
("Некоректна передача даних до банку"),
("Переналаштування ПО");

insert into masters (surname, first_name, patronymic, phone_number) values
("Кава", "Сергій", "Віталійович", "0674512345"),
("Непийпиво", "Андрій", "Андрійович", "0671344256"),
("Мельник", "Руслан", "Владиславович", "0548931568"),
("Шевченко", "Ярослав", "Іванович", "0567843458"),
("Кравець", "Ростислав", "Дмитрович", "0872356185"),
("Іващенко", "Дмитро", "Олександрович", "0783967145"),
("Мороз", "Олександр", "Дмитрович", "0894187564"),
("Кладов", "Антон", "Сергійович", "0895618564"),
("Волков", "Богдан", "Ростиславович", "0893765937"),
("Щіпний", "Іван", "Іванович", "0347818564");

insert into manufactures (name) values
("IBM"),
("Oracle"),
("Huawei"),
("Tercorp"),
("Xiaomi"),
("Samsung"),
("Ericson"),
("Compnal"),
("Terminal"),
("Hyundai");

insert into terminal (shop_id, manufactures_id, date_explotation) values
(4, 4, "2023-07-29"),
(10, 1, "2015-12-13"),
(5,5, "2018-10-10"),
(9, 10, "2019-08-08"),
(10, 3, "2024-01-23"),
(1, 8, "2017-06-27"),
(2, 6, "2020-04-12"),
(6, 2, "2015-05-07"),
(7, 7, "2024-01-05"),
(12, 3, "2019-10-10"),
(3, 5, "2021-01-06"),
(7, 9, "2022-07-04"),
(11, 4, "2023-04-15"),
(1, 1, "2023-10-30"),
(3, 3, "2023-11-03");

insert into service_job (terminal_id, service_type_id, time_start, time_end, date) values
(15, 4, "2024-01-01 17:10:00", "2024-01-01 18:00:00", "2024-01-01"),
(10, 2, "2024-01-01 10:00:00", "2024-01-01 10:30:00", "2024-01-03"),
(7, 9, "2024-01-01 09:30:00", "2024-01-01 10:30:00", "2024-01-05"),
(2, 10, "2024-01-01 13:00:00", "2024-01-01 13:15:00", "2024-01-06"),
(10, 2, "2024-01-01 14:00:00", "2024-01-01 15:30:00", "2024-01-10"),
(14, 6, "2024-01-01 14:00:00", "2024-01-01 15:00:00", "2024-01-11"),
(6, 3, "2024-01-01 15:00:00", "2024-01-01 15:30:00", "2024-01-14"),
(4, 5, "2024-01-01 16:00:00", "2024-01-01 16:30:00", "2024-01-16"),
(2, 1, "2024-01-01 17:00:00", "2024-01-01 17:30:00", "2024-01-17"),
(8, 8, "2024-01-01 12:00:00", "2024-01-01 13:00:00", "2024-01-20"),
(15, 1, "2024-01-01 11:00:00", "2024-01-01 11:15:00", "2024-01-23"),
(3, 10, "2024-01-01 11:00:00", "2024-01-01 12:00:00", "2024-01-26");

insert into service_job_masters (service_job_id, master_id) values
(3, 2),
(12, 9),
(12, 3),
(8, 6),
(9, 9),
(10, 5),
(10, 10),
(10, 4),
(1, 1),
(2, 8),
(4, 3),
(5, 10),
(6, 2),
(7, 9);

insert into invoices (service_job_id, date, total_price) values
(1, "2024-01-03", 100.00),
(2, "2024-01-04", 150.00),
(3, "2024-01-07", 125.00),
(4, "2024-01-08", 150.00),
(5, "2024-01-11", 200.00),
(6, "2024-01-13", 175.00),
(7, "2024-01-16", 200.00),
(8, "2024-01-19", 225.00),
(9, "2024-01-20", 175.00),
(10, "2024-01-22", 500.00),
(12, "2024-01-30", 600.00);


drop procedure if exists get_shops_after_client;
drop procedure if exists get_terminals_after_shop;
drop procedure if exists get_terminals_after_manufacturer;
drop procedure if exists get_service_jobs_after_service_type;
drop procedure if exists get_service_jobs_after_terminal;
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
    select t.shop_id, t.id as terminal_id, sa.street, sa.street_number, sa.gps_latitude, sa.gps_longitude
    from terminal t
    join shop s on t.shop_id = s.id
    join shop_adress sa on s.shop_adress_id = sa.id
    where t.shop_id = shop_id;
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

create procedure get_service_jobs_after_terminal(
	in terminal_id int
	)
begin
	select t.id as terminal_id, sj.id as service_job_id, m.name as manufacturer
	from service_job sj
	join terminal t on sj.terminal_id = t.id
    join manufactures m on t.manufactures_id = m.id
	where sj.terminal_id = terminal_id;
end ///


create procedure get_masters_after_service_jobs(
	in master_id int
    )
begin
	select sjm.id, sjm.service_job_id, m.id as master_id, m.surname, m.phone_number
	from masters m
	join service_job_masters sjm on m.id = sjm.master_id
	where sjm.service_job_id = master_id;

end ///

create procedure get_service_job_after_masters(
	in service_jod_id int
    )
begin
	select sjm.id, sjm.service_job_id, sj.service_type_id
	from service_job sj
	join service_job_masters sjm on sj.id = sjm.master_id
	where sjm.service_job_id = service_jod_id;
end ///

delimiter ;