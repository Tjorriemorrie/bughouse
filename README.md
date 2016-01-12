my masrel project

##RoadMap

- need to load data on payment of org

- how to link payment to actual single org?

- add multiplier of member onto actual time

- how to remove removed members/collaborators and memberships? Periodic hard refresh
or parsing events per repo or hard refresh request from client?

- add and check/distinguish between collaborators and assignees and members (assignees that 
 mibht be collaborators are added as members). Currently i'm making everyone a member :(
 
- share issues by url, currently can't copy&paste links to specific issue

- if removed from org, handle org_selected on client-side approparitetly

- set issue start date, for scheduling with transactional rows for begin and end, then
	aggregate that up to issue. Currently the start date is overwritten everytime
	it gets started :(

- set sessions in db

- link bugs and PRs to branches/issues

- let members set their working hours
- set holidays and time offs for issue timeframing

- auto add public holidays per locale

- generate bell-curve to get percentile intervals for estimation

- delta to github could be by org_id instead of user_id, and then client-side timestamp
can be used to fetch update items instead of response from github, but users have
different permissions and certain data might be omitted

