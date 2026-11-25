--1. Obtén los clientes de brasil 
select * from customer where country = 'Brazil'

--2. Obtén los empleados que son agentes de ventas 
select * from employee where title = 'Sales Support Agent'

--3. Obtén las canciones de ‘AC/DC’ 
select * from track where composer = 'AC/DC'

select * from track as t
join album on track.album_id = album.album_id
join artist on album.artist_id = artist.artist_id
where artist.name = 'AC/DC'
--4. Obtén los campos de los clientes que no sean de USA: Nombre completo, ID, País 
select customer_id as id, first_name ||' '|| last_name as nombre_completo, country as pais 
from customer where country != 'USA'

--5. Obtén los empleados que son agentes de ventas: Nombre completo, Dirección (Ciudad, Estado, País) y email 
select last_name ||' '|| first_name as nombre_completo, address ||', '|| city ||', '|| state ||', '|| country as direccion, email 
from employee where title = 'Sales Support Agent'

--6. Obtén una lista con los países no repetidos a los que se han emitido facturas 
select distinct billing_country from invoice
order by billing_country

--7. Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno. 
--8. Cuántos artículos tiene la factura 37 


--9. Cuántas canciones tiene ‘AC/DC’ 


--10. Cuántos artículos tiene cada factura 


--11. Cuántas facturas hay de cada país 


--12. Cuántas facturas ha habido en 2009 y 2011 


--13. Cuántas facturas ha habido entre 2009 y 2011 


--14. Cuántas clientes hay de España y de Brasil 


--15. Obtén las canciones que su título empieza por ‘You’ 
 
