# EDA--HotelAnalysis-AlmabetterCapstoneProject
## <b> Have you ever wondered when the best time of year to book a hotel room is? Or the optimal length of stay in order to get the best daily rate? What if you wanted to predict whether or not a hotel was likely to receive a disproportionately high number of special requests? This hotel booking dataset can help you explore those questions!

## <b>This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things. All personally identifying information has been removed from the data. </b>

## <b> Explore and analyze the data to discover important factors that govern the bookings. </b>

  ## Understanding The Data
From inital data exploration we see that the dataset consists of both numerical and categorical values. There are even some datetime values stored in the form of object category, which we need to change into proper format. Also there are some categorical variables stored in the form of numerical variables.
  The other thing that we see is that there are some missing values. We will explore the data further and treat the columns with missing values appropriately.
* Lets understand what are the columns:-


1.   **ADR**(*Numeric*): Average Daily Rate defined as - Calculated by dividing the sum of all lodging transactions by the total number of staying nights.
2.   **Adults**(*Integer*): Number of adults
3.   **Agent**(*Categorical*): ID of the travel agency that made the bookings.
4.   **ArrivalDateDayOfMonth**(*Integer*): Day of the month of the arrival date.
5.   **ArrivalDateMonth**(*Categorical*): Month of arrival date with 12 categories (January to December).
6.   **ArrivalDateWeekNumber**(*Integer*):Week number of the arrival date.
7.   **ArrivalDateYear**(*Integer*): Year of arrival date.
8. **AssignedRoomType** (*Categorical*): Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons.
9. **babies** (*Integer*) :Number of babies.
10. **BookingChanges** (*Integer*): Number of changes/amendments made to the booking from the moment the booking was entered on the PMS until the moment of check-in or cancellation.Calculated by adding the number of unique iterations that change some of the booking attributes, namely: persons, arrival date,nights, reserved room type or meal.
11. **Children** (*Integer*): Number of children. Sum of both payable and non-payable children.
12. **Company**(*Categorical*): ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons.
13. **Country**(*Categorical*): Country of origin.
14. **CustomerType**(*Categorical*):Type of booking, assuming one of four
categories:-
*   Contract - when the booking has an allotment or other type of contract associated to it.
*   Group – when the booking is associated to a group
*   Transient – when the booking is not part of a group or contract, and is not associated to other transient booking.
*   Transient-party – when the booking is transient, but is associated to at least other transient booking.
15. **DaysInWaitingList**(*Integer*):Number of days the booking was in the waiting list before it was confirmed to the customer. Calculated by subtracting the date the booking was confirmed to the customer from the date the booking entered on the PMS.
16. **DepositType**(*Categorical*):  Indication on if the customer made a
deposit to guarantee the booking. This variable can assume three categories:-
* No Deposit – no deposit was made.
* Non Refund – a deposit was made in the value of the total stay cost.
* Refundable – a deposit was made with a value under the total cost of stay.
17. **DistributionChannel**(*Categorical*): Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”.
18. **IsCanceled**(*Categorical*): Value indicating if the booking was canceled (1) or not (0).
19. **IsRepeatedGuest**(*Categorical*): Value indicating if the booking name was from a repeated guest (1) or not (0).
20. **LeadTime**(*Integer*): Number of days that elapsed between the entering date of the booking into the PMS and the arrival date. Subtraction of the entering date from the arrival date.
21. **MarketSegment**(*Categorical*): Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”.
22. **Meal**(*Categorical*): Type of meal booked. Categories are presented in standard hospitality meal packages.
* Undefined/SC – no meal package.
* BB – Bed & Breakfast.
* HB – Half board (breakfast and one other meal – usually dinner).
* FB – Full board (breakfast, lunch and dinner)
23. **PreviousBookingsNotCanceled**(*Integer*): Number of previous bookings not cancelled by the customer prior to the current booking.
24. **PreviousCancellations**(*Integer*): Number of previous bookings that were
cancelled by the customer prior to the current booking.
25. **RequiredCardParkingSpaces**(*Integer*): Number of car parking spaces required by the customer.
26. **ReservationStatus**(*Categorical*):Reservation last status, assuming one of three categories:
* Canceled – booking was canceled by the customer.
* Check-Out – customer has checked in but already departed.
* No-Show – customer did not check-in and did inform the hotel of the reason why.
27. **ReservationStatusDate**(*Date*): Date at which the last status was set.
This variable can be used in conjunction with the ReservationStatus to understand when was the booking canceled or when did the customer checked-out of the hotel.
28. **ReservedRoomType**(*Categorical*): Code of room type reserved. Code is
presented instead of designation for anonymity reasons.
29. **StaysInWeekendNights**(*Integer*): Number of weekend nights (Saturday or
Sunday) the guest stayed or booked to stay at the hotel. Calculated by counting the number of weekend nights from the total number of nights.
30. **StaysInWeekNights**(*Integer*): Number of week nights (Monday to Friday the guest stayed or booked to stay at the hotel. Calculated by counting the number of week nights from the total number of nights.
31. **TotalOfSpecialRequests**(*Integer*): Number of special requests made by the customer (e.g. twin bed or high floor). Sum of all special requests.
