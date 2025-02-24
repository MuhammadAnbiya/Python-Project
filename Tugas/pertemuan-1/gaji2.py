rray` or
                `PIL.Image.Image`.
            key_points (KeyPoints): A collection of key points where each key point
                consists of x and y coordinates.
            labels (List[str], optional): A list of labels to be displayed on the
                annotated image. If not provided, keypoint indices will be used.

        Returns:
            The annotated image, matching the type of `scene` (`numpy.ndarray`
                or `PIL.Image.Image`)

        Example:
            ```python
            import supervision as sv

            image = ...
            key_points = sv.KeyPoints(...)

            vertex_label_annotator = sv.VertexLabelAnnotator(
                color=sv.Color.GREEN,
     