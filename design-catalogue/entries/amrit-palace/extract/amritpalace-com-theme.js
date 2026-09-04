// React Theme — extracted from https://amritpalace.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '176.64': string;
    '102.4': string;
    '61.44': string;
    '57.6': string;
    '44.8': string;
    '37.12': string;
    '23.04': string;
    '19.2': string;
    '13.44': string;
    '12.8': string;
    '12.096': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '52': string;
    '62': string;
    '78': string;
    '90': string;
    '128': string;
    '147': string;
    '174': string;
    '202': string;
    '232': string;
    '245': string;
    '250': string;
    '275': string;
    '280': string;
    '320': string;
 *   };
 *   radii: {
    xs: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#d49653",
    "secondary": "#d8cbb8",
    "background": "#d8cbb8",
    "foreground": "#000000",
    "neutral50": "#2c2c2c",
    "neutral100": "#000000",
    "neutral200": "#dfdad5",
    "neutral300": "#222222",
    "neutral400": "#efefef",
    "neutral500": "#bfb4a3"
  },
  "fonts": {
    "body": "'webflow-icons', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "176.64": "176.64px",
    "102.4": "102.4px",
    "61.44": "61.44px",
    "57.6": "57.6px",
    "44.8": "44.8px",
    "37.12": "37.12px",
    "23.04": "23.04px",
    "19.2": "19.2px",
    "13.44": "13.44px",
    "12.8": "12.8px",
    "12.096": "12.096px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "52": "52px",
    "62": "62px",
    "78": "78px",
    "90": "90px",
    "128": "128px",
    "147": "147px",
    "174": "174px",
    "202": "202px",
    "232": "232px",
    "245": "245px",
    "250": "250px",
    "275": "275px",
    "280": "280px",
    "320": "320px"
  },
  "radii": {
    "xs": "2px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#d49653",
      "light": "hsl(31, 60%, 73%)",
      "dark": "hsl(31, 60%, 43%)"
    },
    "secondary": {
      "main": "#d8cbb8",
      "light": "hsl(36, 29%, 93%)",
      "dark": "hsl(36, 29%, 63%)"
    },
    "background": {
      "default": "#d8cbb8",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#2c2c2c"
    }
  },
  "typography": {
    "fontFamily": "'Satoshi', sans-serif",
    "h1": {
      "fontSize": "37.12px",
      "fontWeight": "500",
      "lineHeight": "37.12px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": []
};

export default theme;
