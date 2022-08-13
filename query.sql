SELECT id, name
FROM events
WHERE id IN (SELECT event_id
             FROM event_attendees
             WHERE person_id = '5e7f0918-a2c0-41e7-8e7b-ae5f65fbb47c'
             LIMIT 4);


SELECT id, capacity_required
FROM events
WHERE id IN (SELECT event_id
             FROM event_attendees
             WHERE person_id = '5e7f0918-a2c0-41e7-8e7b-ae5f65fbb47c'
             LIMIT 4);