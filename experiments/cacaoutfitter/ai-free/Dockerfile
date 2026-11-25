ARG WAYPOINT_BASE=educloud-waypoint-course:af44909f8a07
FROM ${WAYPOINT_BASE}
USER root
COPY *.whl /tmp/concept-panel/
RUN python -m pip install --no-index --no-deps /tmp/concept-panel/*.whl && rm -r /tmp/concept-panel
COPY --chown=1000:1000 learner/ /home/learner/work/
USER 1000:1000
