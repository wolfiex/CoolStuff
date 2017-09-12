program pi
use mpi_f08
implicit none 

integer :: rank, size, len,ierr,counter
integer :: name_length

character(len=MPI_MAX_PROCESSOR_NAME) :: processor_name
character(len=mpi_max_library_version_string)::vers

integer::n, i ,j 
integer, parameter :: qp = selected_real_kind (32)!real*16
integer :: newtype
real(kind = qp):: ans , sumans, ans0
real(kind = 8):: ansdp

type(mpi_status)::status
call MPI_INIT(ierr)
!call mpi_type_create_f90_real(32, MPI_UNDEFINED, NEWTYPE, ierr)
call mpi_comm_rank(Mpi_comm_world,rank,ierr)
call mpi_comm_size(Mpi_comm_world,size,ierr)
call MPI_Get_processor_name(processor_name,name_length,ierr)
call MPI_GET_LIBRARY_VERSION(vers, len,ierr)

!print *, 'now running', trim(vers)





n= 840
ans = 0 
counter = 0

do i=1,n,n/size
		
		!print*, i , (i + n/size-1)
		
		if (counter == rank) then 
			do j=i, (i + n/size-1)
				ans = ans + 1./(1.+((j-.5)/n)**2)
			end do

			if (rank .ne. 0 ) call MPI_SEND(ans,storage_size(ans)/8,MPI_BYTE, 0, counter, Mpi_comm_world,ierr)
		end if 

		counter = counter + 1
end do



if (rank ==0 ) then 
	ans0 = ans

	do i=1,size-1
	call MPI_RECV (sumans, storage_size(ans)/8, MPI_BYTE,mpi_any_source , mpi_any_tag, Mpi_comm_world, status)
	ans0 = ans0+sumans	
	end do 

	print*, 4*ans0/n
	
	
end if

!reduce cant be on node 

ansdp= real(ans)
print*, ansdp
call MPI_REDUCE(ansdp, sumans,1, MPI_DOUBLE, MPI_SUM, 0, Mpi_comm_world)
if (rank ==0) print*, ans ,sumans,  4* (ans + sumans)/n




call mpi_finalize(ierr)
end program pi
