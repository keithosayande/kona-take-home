"use client";
import { FilePond } from "react-filepond";

// Import FilePond styles
import "filepond/dist/filepond.min.css";

import { useState } from "react";

export default function Home() {
  const [files, setFiles] = useState([]);

  return (
    <div className="grid min-h-screen w-full grid-cols-1 gap-8 p-6 md:grid-cols-2 md:p-10 lg:p-12">
      <div className="flex flex-col items-start gap-6 rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
        <div className="space-y-2">
          <h2 className="text-xl font-semibold">Upload Documents</h2>
          <div className="w-full">
            <FilePond
              files={files}
              onupdatefiles={setFiles}
              allowMultiple={false}
              maxFiles={1}
              server="/api/upload"
              name="file"
              labelIdle='Drag & Drop your files or <span class="filepond--label-action">Browse</span>'
            />
          </div>
        </div>
      </div>
      
    </div>
  );
}
