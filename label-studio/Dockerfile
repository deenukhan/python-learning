# Use the official Label Studio image
FROM heartexlabs/label-studio:latest

# Set environment variables
ENV LABEL_STUDIO_PORT 8080
ENV LABEL_STUDIO_HOME /label-studio

# Create a directory for Label Studio data and set it as a volume
RUN mkdir -p $LABEL_STUDIO_HOME/data
VOLUME $LABEL_STUDIO_HOME/data

# Expose the Label Studio port
EXPOSE $LABEL_STUDIO_PORT

# Start Label Studio
CMD ["label-studio", "start", "--host", "0.0.0.0", "--port", "$LABEL_STUDIO_PORT"]
