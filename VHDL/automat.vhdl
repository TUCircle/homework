
library ieee; 
use ieee.std_logic_1164.all; 


entity Testbench is end entity; 

architecture Test of Testbench is 
 signal T, I: std_logic;
 signal x, y: std_logic;
 signal s: std_logic_vector(2 downto 0);
begin 

 Samblingprocess: process(T, I)
 begin
  if I= '1' then
   s <= "000";
  elsif rising_edge(T) then
	 y <= not(x) and not(s(1));
	 s(2) <= not(not(s(1) and s(2)) and not( s(2) and not(x)) and not(s(1) and not(s(0)) and not(x)));
	 s(1) <= not(not(s(2) and not(x)) and not( s(2) and not(s(1))) and not(s(1) and x and not(s(0))) and not(s(0) and x and not(s(1))) and not(not(s(1)) and not(x) and not(s(0))) and not(s(1) and not(x)));
	 s(0) <= not(not(s(0) and not(x)) and not(x and not(s(0))) and not(x and not(s(0)) and not(s(1)) and not(s(2))) and not(s(2) and not(x)));
  end if;
 end process;

end architecture;

